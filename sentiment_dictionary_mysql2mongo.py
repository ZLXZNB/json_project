# -*- coding: utf-8 -*-
"""
@File       : text_library_mysql2mongo.py
@Author     : Yuka
@Time       : 2021/1/7 14:53
@Version    : 1.0.0
@Description:
"""

import json

import mysql.connector.pooling
import pymongo


def string_to_list(a):
    if a.split(','):
        return a.split(',')
    else:
        return [a]


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
    "mongodb://monetware:monetware2020%40sh.com@222.95.98.219:20000/admin?connectTimeoutMS=10000&authSource=admin")
db = client["ring_service_v2"]
collection = db["rs_sentiment_dictionary"]
for name in tables:
    print(name)
    labels = []
    # project_id = re.findall("rs_textlibrary_data_(\d+)$", name)[0]
    sql = "SELECT " \
          "a.`name`, " \
          "a.create_user, " \
          "a.create_time, " \
          "b.word, " \
          "b.score " \
          "FROM " \
          "rs_analysis_sentiment_dictionary a, " \
          "rs_analysis_sentiment_dictionary_word b " \
          "WHERE " \
          "a.id = b.dictionary_id "
    cursor.execute(sql)
    print("sql执行完成")
    buffer = []
    all_sentiment_dictionary = []
    count = 0
    for record in cursor:
        all_sentiment_dictionary.append(record)
        if record["name"] not in labels:
            labels.append(record["name"])
    print(labels)
    for label in labels:
        positive = []
        negative = []
        create_user = ""
        create_time = None
        for record in all_sentiment_dictionary:
            if record["name"] == label:
                print("找到相同的")
                create_user = record["create_user"]
                create_time = record["create_time"]
                if record["score"] is not None:
                    if record["score"] > 0:
                        positive.append(record["word"])
                    else:
                        negative.append(record["word"])

        sentiment_dictionary = {"name": label, "create_user": create_user, "create_time": create_time,
                                "positive": positive, "negative": negative}

        count += 1
        buffer.append(sentiment_dictionary)
        if len(buffer) >= 2000:
            collection.insert_many(buffer)
            buffer.clear()
            print("insert 2000...")
    if count < 1:
        continue
    if len(buffer) > 0:
        collection.insert_many(buffer)
        print("insert {}...".format(len(buffer)))
        buffer.clear()
    print("{}：迁移了{}条数据".format(name, count))

client.close()
