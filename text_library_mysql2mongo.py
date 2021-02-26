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
cursor = connection.cursor(dictionary=True, bufferd=True)

cursor.execute('SHOW TABLES')
import re

# tables = [name["Tables_in_ringanalyzer"]
#           for name in cursor.fetchall()
#           if re.match("rs_textlibrary_data_(\d+)$", name["Tables_in_ringanalyzer"])]
tables = ["rs_analysis_define_library"]
client = pymongo.MongoClient(
    "mongodb://monetware:monetware2020%40sh.com@222.95.98.219:20000/admin?connectTimeoutMS=10000&authSource=admin")
db = client["ring_service_v2"]
collection = db["rs_seg_config"]
for name in tables:
    # project_id = re.findall("rs_textlibrary_data_(\d+)$", name)[0]
    sql = "select * from " + name
    print(name)
    cursor.execute(sql)
    buffer = []
    count = 0
    for record in cursor:
        if record["is_delete"] == 1:
            record["is_delete"] = False
        else:
            record["is_delete"] = True
        count += 1
        buffer.append(record)
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
