# -*- coding: utf-8 -*-
"""
@File       : text_library_mysql2mongo.py
@Author     : Yuka
@Time       : 2021/1/7 14:53
@Version    : 1.0.0
@Description:
"""

import json
import xlsxwriter
import mysql.connector.pooling
import pymongo


def string_to_list(a):
    if a.split(','):
        return a.split(',')
    else:
        return [a]


name_list = ["BosonNLP", "台湾大学情感词典", "大连理工大学中文情感", "清华大学中文褒贬义词典", "知网Hownet情感词典"]

DBS = {
    "host": "rm-uf6x8t115nb94hrak9o.mysql.rds.aliyuncs.com",
    # "host": "49.74.204.242",
    "port": 3306,
    "user": "ringdata_web",
    # "user": "root",
    # "password": "monetware",
    "password": "ringdata2019@sh",
    "database": "ringanalyzer",
    "charset": "utf8"
}

pool = mysql.connector.pooling.MySQLConnectionPool(**DBS, pool_size=10, pool_name="pool")
connection = pool.get_connection()
cursor = connection.cursor(dictionary=True, buffered=True)

cursor.execute('SHOW TABLES')
import re

# tables = [name["Tables_in_ringanalyzer"]
#           for name in cursor.fetchall()
#           if re.match("rs_textlibrary_data_(\d+)$", name["Tables_in_ringanalyzer"])]
tables = ["rs_analysis_sentiment_dictionary"]
client = pymongo.MongoClient(
    "mongodb://monetware:monetware2020%40sh.com@49.74.204.78:20000/admin?connectTimeoutMS=10000&authSource=admin")
db = client["ring_service_v2"]
collection = db["rs_sentiment_dictionary"]
for x in collection.find():
    print(x["name"])
    if x["name"] in name_list:
        file_result = "D:/sentiment_dictionary/" + x["name"] + ".xlsx"
        workbook_result = xlsxwriter.Workbook(file_result)
        worksheet_result_positive = workbook_result.add_worksheet('积极词')
        worksheet_result_negative = workbook_result.add_worksheet('消极词')
        positive = x["positive"]
        negative = x["negative"]
        worksheet_result_positive.write(0, 0, "积极词")
        worksheet_result_negative.write(0, 0, "消极词")
        for i in range(len(positive)):
            worksheet_result_positive.write(i+1, 0, positive[i])
            print("写入成功")
        for i in range(len(negative)):
            worksheet_result_negative.write(i + 1, 0, negative[i])
            print("写入成功")
        workbook_result.close()

