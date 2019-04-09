from pyspark import SparkContext
from pyspark.sql import SparkSession

# 初始化一个SparkSession，该对象是SparkContext和SQLContext等的集合
spark = SparkSession.\
    builder.\
    appName("Python Spark SQL basic example").\
    master("local[*]").\
    config("spark.some.config.option", "some-value").\
    config('spark.debug.maxToStringFields', '50'). \
    getOrCreate()

# 初始化SparkContext
sc = SparkContext.getOrCreate()

## SparkDataFrame基本操作
flightPrefFilePath = "C:\\Users\\WS\\Desktop\\departuredelays.csv"
airPortsFilePath = "C:\\Users\\WS\\Desktop\\airport-codes-na.txt"

airports = spark.read.csv(airPortsFilePath, header=True, sep="\t", inferSchema=True)
airports.createOrReplaceTempView("airports")
flightPref = spark.read.csv(flightPrefFilePath, header=True)
flightPref.createGlobalTempView("FlightPerformance")

flightPref.cache()

spark.sql("""
    select a.city, f.origin, sum(f.delay) as Delays
    from airports a 
    join FlightPerformance f
    on a.IATA=f.origin
    where a.state='WA'
    group by a.city, f.origin
    order by sum(f.delay) desc
""").show()


spark.sql("""
    select a.state,sum(f.delay) as Delays
    from airports a 
    join FlightPerformance f
    on a.IATA=f.origin
    where a.country='USA'
    group by a.state
""").show()

## 处理重复数据
df = spark.createDataFrame([
    (1, 144.5, 5.9, 33, 'M'),
    (2, 167.2, 5.4, 45, 'M'),
    (3, 124.1, 5.2, 23, 'F'),
    (4, 144.5, 5.9, 33, 'M'),
    (5, 133.2, 5.7, 54, 'F'),
    (3, 124.1, 5.2, 23, 'F'),
    (5, 129.2, 5.3, 43, 'M')
], ["id", "weight", "height", "age", "gender"])

print("Count the rows: {0}".format(df.count()))
print("Count the distinct rows:{0}".format(df.distinct().count()))

df = df.dropDuplicates()

print("Count the rows: {0}".format(df.count()))
print("Count the distinct rows:{0}".format(df.select([i for i in df.columns if i != "id"]).distinct().count()))

df = df.dropDuplicates(subset=[c for c in df.columns if c != "id"])

import pyspark.sql.functions as fn

df.agg(
    fn.count('id').alias("count"),
    fn.countDistinct('id').alias("distinct")
).show()

df.withColumn("new_id", fn.monotonically_increasing_id()).show()

## 处理缺失值
df_miss = spark.createDataFrame([
    (1, 143.5, 5.6, 28, 'M', 100000),
    (2, 167.2, 5.4, 45, 'M', None),
    (3, None, 5.2, None, None, None),
    (4, 144.5, 5.9, 33, 'M', None),
    (5, 133.2, 5.7, 54, 'F', None),
    (6, 124.1, 5.2, None, 'F', None),
    (7, 129.2, 5.3, 42, 'M', 76000)
], ["id", "weight", "height", "age", "gender", "income"])

df_miss.rdd.map(lambda row: (row["id"], sum([c == None for c in row]))).collect()

# agg后面的*号表示将DataFrame按列处理，也就是在拿出列名c之后，直接可以计算c列的均值、最大值等等信息。
df_miss.agg(*[
    (1 - (fn.count(c) / fn.count("*"))).alias(c + "_missing")
    for c in df_miss.columns
]).show()

df_miss_no_income = df_miss.select([c for c in df_miss.columns if c != "income"])
df_miss_no_income.dropna(thresh=3).show()

means = df_miss_no_income.agg(*[
    fn.mean(c).alias(c)
    for c in df_miss_no_income.columns if c != "gender"
]).toPandas().to_dict("records")[0]
df_miss_no_income.fillna(means).show()

## 异常值处理(四分位法)
df_outliers = spark.createDataFrame([
    (1, 143.5, 5.3, 28),
    (2, 154.2, 5.5, 45),
    (3, 342.3, 5.1, 99),
    (4, 144.5, 5.5, 33),
    (5, 133.2, 5.4, 54),
    (6, 124.1, 5.1, 21),
    (7, 129.2, 5.3, 42)
], ["id", "weight", "height", "age"])

cols = ["weight", "height", "age"]
bounds = {}

for col in cols:
    quantiles = df_outliers.approxQuantile(col, [0.25, 0.75], 0.05)
    IQR = quantiles[1] - quantiles[0]
    bounds[col] = [quantiles[0] - 1.5*IQR, quantiles[1] + 1.5*IQR]

outliers = df_outliers.select(*["id"] + [
    ((df_outliers[c] < bounds[c][0]) | (df_outliers[c] > bounds[c][1])).alias(c + "_o")
    for c in cols]
)
outliers.show()


