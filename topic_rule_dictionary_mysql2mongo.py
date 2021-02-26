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


def topic_rule(topic):
    topic_1 = topic.replace("AND", "&")
    topic_2 = topic_1.replace("and", "&")
    topic_3 = topic_2.replace("OR", "|")
    topic_4 = topic_3.replace("or", "|")
    topic_5 = topic_4.replace("+", "")
    return topic_5


cursor.execute('SHOW TABLES')
import re

# tables = [name["Tables_in_ringanalyzer"]
#           for name in cursor.fetchall()
#           if re.match("rs_textlibrary_data_(\d+)$", name["Tables_in_ringanalyzer"])]
tables = ["rs_analysis_subject_library"]
client = pymongo.MongoClient(
    "mongodb://monetware:monetware2020%40sh.com@222.95.98.219:20000/admin?connectTimeoutMS=10000&authSource=admin")
db = client["ring_service_v2"]
collection = db["rs_topic_rule_dictionary"]
for name in tables:
    print(name)
    labels = []
    # project_id = re.findall("rs_textlibrary_data_(\d+)$", name)[0]
    sql = "SELECT a.`name`, a.`create_user`,a.`create_user`,a.`create_time`, " \
          "b.`name` as `logic_name`,b.logic " \
          "FROM rs_analysis_subject_library a, rs_analysis_subject_library_data b " \
          "WHERE a.id = b.sub_id; "
    cursor.execute(sql)
    print("sql执行完成")
    buffer = []
    all_topic_rule_dictionary = []
    count = 0
    for record in cursor:
        all_topic_rule_dictionary.append(record)
        if record["name"] not in labels:
            labels.append(record["name"])
    print(labels)
    for label in labels:
        topic_rules = {}
        create_user = ""
        create_time = None
        for record in all_topic_rule_dictionary:
            if record["name"] == label:
                print("找到相同的")
                logic = record["logic"]
                new_logic = topic_rule(logic)
                topic_rules[record["logic_name"]] = new_logic
                create_user = record["create_user"]
                create_time = record["create_time"]

        topic_rule_dictionary = {"name": label, "create_user": create_user, "create_time": create_time,
                                 "topic_rules": topic_rules}

        count += 1
        buffer.append(topic_rules)
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
