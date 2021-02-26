# 关键词词共现
# -*- coding: utf-8 -*-
"""
@File       : text_library_mysql2mongo.py
@Author     : Yuka
@Time       : 2021/1/7 14:53
@Version    : 1.0.0
@Description:
"""
import numpy as np
import pyperclip
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from textrank4zh import TextRank4Sentence
import json
import xlsxwriter
import mysql.connector.pooling
import pymongo
from bert_serving.client import BertClient
import numpy as np
import matplotlib.pyplot as plt
import xlrd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import font_manager


def sort_dict_by_value(d, reverse=True):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))


# file_3 = 'D:/monetwaredata/biology_co.xlsx'
# workbook_3 = xlsxwriter.Workbook(file_3)
# worksheet_3 = workbook_3.add_worksheet('Sheet1')
# word_art_file = "D:/monetwaredata/wordart.xlsx"
# workbook = xlsxwriter.Workbook(word_art_file)
# worksheet = workbook.add_worksheet('Sheet1')
# client = pymongo.MongoClient("mongodb://192.168.1.142:27017/admin?connectTimeoutMS=10000&authSource=admin")
# db = client["biology"]
# collection = db["biology_data"]
# word_cloud_dictionary = {}
# for x in collection.find():
#     if "keyword" in x.keys():
#         keywords = x["keyword"]
#         for word in keywords:
#             if word in word_cloud_dictionary:
#                 word_cloud_dictionary[word] += 1
#             else:
#                 word_cloud_dictionary[word] = 1
#
# final_result = sort_dict_by_value(word_cloud_dictionary)
# print(len(final_result.keys()))
# keys_list = list(final_result.keys())
# for i in range(len(keys_list)):
#     print(i)
#     worksheet.write(i, 0, keys_list[i])
#     worksheet.write(i, 1, final_result[keys_list[i]])
#
# workbook.close()
# print(final_result)
# labels = []
# for i in range(0, 500):
#     labels.append(keys_list[i])
#
# bc = BertClient("wx.ringdata.net", port=15555, port_out=15556)
#
# for label in labels:
#     if label != '':
#         vector = bc.encode([label])
#         print(vector)

wb = xlrd.open_workbook('D:/monetwaredata/biology_co_en_coefficient.xlsx')
sh = wb.sheet_by_name('Sheet1')
my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/simsun.ttc")
final_result = []
for i in range(1, 201):
    if sh.cell(i, 0).value != "\xa0":
        final_result.append(sh.cell(i, 0).value)
# bc = BertClient("wx.ringdata.net", port=15555, port_out=15556)
# vector = bc.encode(final_result)
# print(vector)
# print(len(vector))
vector = []
for i in range(1, 201):
    if sh.cell(i, 0).value != "\xa0":
        word_vector = []
        for j in range(1, 201):
            word_vector.append(sh.cell(i, j).value)
        vector.append(word_vector)
sparse_vector = TSNE(n_components=2, learning_rate=200).fit_transform(vector)
colors_all = [
    '#37A2DA', '#e06343', '#37a354', '#b55dba', '#b5bd48', '#8378EA', '#96BFFF',
    '#6F4242', '#FF00FF', '#97694F', '#6B8E23', '#BC1717', '#00FFFF', '#7093DB', '#EAEAAE', '#238E68',
    '#FFFF00', '#855E42', '#9370DB', '#6B4226', '#545454', '#426F42', '#8E6B23', '#856363'
]
print("二维数组为")
print(sparse_vector.tolist())
print("标签为")
print(final_result)
# {value:[10.0, 8.04],name:"dsada",label:{show:true, formatter:"好"},itemStyle:{color:"#00FF7F"}},
all_result = []
for i in range(len(final_result)):
    temporary_result = [final_result[i]]
    for value in sparse_vector.tolist()[i]:
        temporary_result.append(value)
    all_result.append(temporary_result)
print("综合结果为")
print(all_result)


# for label in labels:
#     if label != '':
#         vector = bc.encode([label])
#         print(vector)
# vectors = TSNE(n_components=3, learning_rate=200).fit_transform(final_result)
# print(vectors)
# x = []
# y = []
# z = []
# for vector in vectors:
#     x.append(vector[0])
#     y.append(vector[1])
#     z.append(vector[2])
# ax1 = plt.axes(projection='3d')
# ax1.plot3D(x, y, z, '*')
# text = ['疫情中的众生相', '防控部署', '医疗物资保障与基础设施建设', '疫情中的经济', '疫情中的文化传播', '疫情中的民生', '新冠肺炎医治', '疫情中的国际社会', '新冠疫情动态', '疫情中的法制']
# for i in range(len(x)):
#     ax1.text(x[i], y[i], z[i], text[i], fontsize=12, fontproperties=my_font)
# plt.show()
def k_means_cluster(text_vectors, cluster_number):
    model = KMeans(n_clusters=cluster_number)
    model.fit(text_vectors)
    yhat = model.predict(text_vectors)
    return yhat.tolist()


cluster_number = 20
cluster_result = []
result = k_means_cluster(vector, cluster_number)
for i in range(cluster_number):
    category = []
    for j in range(len(result)):
        if result[j] == i:
            category.append(final_result[j])
    cluster_result.append(category)
for cluster in cluster_result:
    print(cluster)

sparse_cluster_result = []
result_sparse = k_means_cluster(sparse_vector, cluster_number)
for i in range(cluster_number):
    category_sparse = []
    for j in range(len(result_sparse)):
        if result_sparse[j] == i:
            category_sparse.append(final_result[j])
    sparse_cluster_result.append(category_sparse)

echarts_result = []
# {value:[10.0, 8.04],name:"dsada",label:{show:true, formatter:"好"},itemStyle:{color:"#00FF7F"}},
for i in range(len(final_result)):
    echarts_json = {"name": final_result[i], "value": sparse_vector.tolist()[i],
                    "label": {"show": "true", "formatter": final_result[i]}}
    for j in range(len(cluster_result)):
        if final_result[i] in cluster_result[j]:
            echarts_json["itemStyle"] = {"color": colors_all[j]}
    echarts_result.append(echarts_json)
pyperclip.copy(json.dumps(echarts_result, ensure_ascii=False))
print("画图结果为")
print(echarts_result)
