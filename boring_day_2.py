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

'''
data = sc.parallelize(
    [
        ("Amber", 22), ("Alfred", 23), ("Skye", 4), ("Albert", 12), ("Amber", 9)
    ]
)
print(data.collect())

data_heterogenous = sc.parallelize(
    [
        ("Fruit", "Apple"),
        {"score": 98},
        [23, 'feel', False, None]
    ]
)
print(data_heterogenous.collect())

fileData = sc.textFile("C:\\Users\\WS\\Desktop\\new 1.txt")
print(type(fileData))


rdd1 = sc.parallelize([("a", 1), ("b", 4), ("c", 10)])
rdd2 = sc.parallelize([("a", 1), ("a", 1), ("b", 6), ("d", 15)])
rdd3 = rdd1.leftOuterJoin(rdd2)
print(rdd3.collect())
'''

stringCSVRDD = sc.parallelize((
    {"id":123,"name":"Katie","age":19,"eyeColor": "brown"},
    {"id": 234,"name": " Michael","age":22,"eyeColor": "green"},
    {"id": 345,"name": "Simone","age": 23,"eyeColor": "blue"}
))
from pyspark.sql.types import *
schema = StructType([
    StructField("id", LongType(), True),
    StructField("name", StringType(), True),
    StructField("age", LongType(), True),
    StructField("eyeColor", StringType(), True)
])


