# 关键词词共现
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


def sort_dict_by_value(d, reverse=True):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))


file_3 = 'D:/monetwaredata/biology_co_en_coefficient.xlsx'
workbook_3 = xlsxwriter.Workbook(file_3)
worksheet_3 = workbook_3.add_worksheet('Sheet1')

#
#
# def string_to_list(a):
#     if a.split(','):
#         return a.split(',')
#     else:
#         return [a]
#
#
# name_list = ["BosonNLP", "台湾大学情感词典", "大连理工大学中文情感", "清华大学中文褒贬义词典", "知网Hownet情感词典"]
#
# DBS = {
#     "host": "rm-uf6x8t115nb94hrak9o.mysql.rds.aliyuncs.com",
#     # "host": "49.74.204.242",
#     "port": 3306,
#     "user": "ringdata_web",
#     # "user": "root",
#     # "password": "monetware",
#     "password": "ringdata2019@sh",
#     "database": "ringanalyzer",
#     "charset": "utf8"
# }
#
# pool = mysql.connector.pooling.MySQLConnectionPool(**DBS, pool_size=10, pool_name="pool")
# connection = pool.get_connection()
# cursor = connection.cursor(dictionary=True, buffered=True)
#
# cursor.execute('SHOW TABLES')
import re

# tables = [name["Tables_in_ringanalyzer"]
#           for name in cursor.fetchall()
#           if re.match("rs_textlibrary_data_(\d+)$", name["Tables_in_ringanalyzer"])]
# tables = ["rs_analysis_sentiment_dictionary"]
# word_art_file = "D:/monetwaredata/wordart.xlsx"
# workbook = xlsxwriter.Workbook(word_art_file)
# worksheet = workbook.add_worksheet('Sheet1')
client = pymongo.MongoClient("mongodb://192.168.1.142:27017/admin?connectTimeoutMS=10000&authSource=admin")
db = client["biology"]
collection = db["biology_data"]
word_cloud_dictionary = {}
for x in collection.find():
    if "keyword" in x.keys() and x["type"] == "english":
        keywords = x["keyword"]
        for word in keywords:
            if word is not None and word != "":
                if word in word_cloud_dictionary:
                    word_cloud_dictionary[word] += 1
                else:
                    word_cloud_dictionary[word] = 1

final_result = sort_dict_by_value(word_cloud_dictionary)
# print(len(final_result.keys()))
keys_list = list(final_result.keys())
# for i in range(len(keys_list)):
#     print(i)
#     worksheet.write(i, 0, keys_list[i])
#     worksheet.write(i, 1, final_result[keys_list[i]])
#
# workbook.close()
# print(final_result)
labels = []
for i in range(0, 200):
    labels.append(keys_list[i])

dict_first = {}
self_co = [0] * len(labels)
count_map = {"none": {}}
for i in range(len(labels)):
    dic_two = {}
    for j in range(i + 1, len(labels)):
        dic_two[labels[j]] = 0
    dict_first[labels[i]] = dic_two

number = 0
for x in collection.find():
    if "keyword" in x.keys() and x["type"] == "english":
        keywords = x["keyword"]
        number = number + 1
        print(number)
        for i in range(len(labels)):
            for j in range(i + 1, len(labels)):
                if labels[i] in keywords and labels[j] in keywords:
                    print('匹配成功')
                    dict_first[labels[i]][labels[j]] += 1
            if labels[i] in keywords:
                self_co[i] += 1
for i in range(len(labels)):
    worksheet_3.write(i + 1, 0, labels[i])
    worksheet_3.write(0, i + 1, labels[i])
    worksheet_3.write(i + 1, i + 1, 1)
    for j in range(i + 1, len(labels)):
        worksheet_3.write(i + 1, j + 1, dict_first[labels[i]][labels[j]] / self_co[i])
    for m in range(1, i + 1):
        worksheet_3.write(i + 1, m, dict_first[labels[m - 1]][labels[i]] / self_co[i])
workbook_3.close()
