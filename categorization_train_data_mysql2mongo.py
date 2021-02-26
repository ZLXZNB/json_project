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
cursor = connection.cursor(dictionary=True, buffered=True)

cursor.execute('SHOW TABLES')
import re

# tables = [name["Tables_in_ringanalyzer"]
#           for name in cursor.fetchall()
#           if re.match("rs_textlibrary_data_(\d+)$", name["Tables_in_ringanalyzer"])]
#
# classify_model_table_name = [name["Tables_in_ringanalyzer"]
#                              for name in cursor.fetchall()
#                              if name == "rs_analysis_classify_model"]
# classify_category_table_name = [name["Tables_in_ringanalyzer"]
#                                 for name in cursor.fetchall()
#                                 if name == "rs_analysis_classify_model_category"]
classify_text_table_name = ["rs_analysis_classify_model_text"]
print(classify_text_table_name)
client = pymongo.MongoClient(
    "mongodb://monetware:monetware2020%40sh.com@222.95.98.219:20000/admin?connectTimeoutMS=10000&authSource=admin")
db = client["ring_service_v2"]
collection = db["rs_text_categorization_train_data"]
for name in classify_text_table_name:
    print(name)
    # _id = re.findall("rs_analysis_classify_model_text(\d+)$", name)[0]
    sql = "SELECT a.content as content, " \
          "a.model_id as train_data_id, " \
          "a.category_id as label_id, " \
          "b.name as label, " \
          "c.name as train_data_name, " \
          "c.create_user as create_user, " \
          "c.create_time as create_time " \
          "FROM rs_analysis_classify_model_text a, rs_analysis_classify_model_category b, rs_analysis_classify_model c " \
          "WHERE a.model_id = b.model_id and a.category_id = b.id and a.model_id = c.id "
    cursor.execute(sql)
    print("sql语句执行完成")
    buffer = []
    count = 0
    for record in cursor:
        # if record["is_delete"] == 1:
        #     record["is_delete"] = False
        # else:
        #     record["is_delete"] = True
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
