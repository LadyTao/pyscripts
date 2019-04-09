

import pickle, pprint

# data1 = {"a": [1,2.0,3,4+6j], "b": ("string", u'Unicode String'), "c": None}
#
# selfref = [1, 2, 3]
# selfref.append(selfref)

# output = open("C:\\Users\\WS\\Desktop\\data.pkl", "wb")
# pickle.dump(data1, output)
# pickle.dump(selfref, output, -1)
# output.close()
#
# pkl_file = open("C:\\Users\\WS\\Desktop\\data.pkl", "rb")
# data1 = pickle.load(pkl_file)
# print(data1)
#
# data2 = pickle.load(pkl_file)
# print(data2)
# print(pkl_file.tell())
# pkl_file.close()


# try:
#     x = int(input("please input a number:"))
#     print(x)
# except ValueError:
#     print("invalid input!")
# else:
#     print("------------------+++++++++++++++++++++")
# print("----------------------------------------")
#
#
# print("+++++++++++++++++++++++++++++++++++++++++++++")

# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("divided by Zero!")
#     except:
#         print("there are still Exception!")
#     else:
#         print("the result is {}".format(result))
#     finally:
#         print("executing finally clause")

# import os
# print(os.getcwd())
# print(dir(os))
# print(help(os))


# import re
# x = re.match(r"^\d{3}\-\d{3,8}$", "010-12345")
# print(x)
#
# y = re.match(r"^\d{3}\-\d{3,8}$", "010 12345")
# print(y)
#
# s = "a b        c"
# print(s.split(" "))
# print(re.split("\s+", s))
#
#
# m = re.match(r"^(\d{3})\-(\d{3,8})$", "010-123456")
# print(m)
# print(m.group(0), m.group(1), m.group(2), m.groups())
#
# n = re.match(r"^(\d+)(0*)$", "234000")
# print(n.groups())
#
# nx = re.match(r"^(\d+?)(0*)$", "234000")
# print(nx.groups())
#
#
# email1 = "someone@gmail.com"
# email2 = "bill.gates@microsoft.com"
# email3 = "someone@qq.com"
# email4 = "23rtrb_-sz@gmail.com"
# email5 = "@gmail.com"
#
# r = re.match(r"^([a-z|A-Z|0-9_\_|\-]+)(@gmail.com|@microsoft.com)$", email4)
# print(r)

# import pymysql
# db = pymysql.connect(host="192.168.11.82", user="********", password="*********", database="f_user", port=3308)
# cursor = db.cursor()
# cursor.execute("SELECT * FROM f_user.wx_member limit 100")
# data = cursor.fetchone()
# print(data)
# db.close()

# import json

import time,calendar
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strptime("2019-04-08 14:39:21", "%Y-%m-%d %H:%M:%S"))
print(time.asctime(time.strptime("2019-04-08 14:39:21", "%Y-%m-%d %H:%M:%S")))
# for i in range(1,13):
#     print("---2019年{}月日历---".format(i))
#     print(calendar.month(2019, i))







