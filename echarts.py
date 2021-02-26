import csv
import xlsxwriter
import pandas as pd
import math
import json
import xlrd

import pyperclip

csv_reader = csv.reader(open('D:/new_co/11_co_label.csv', encoding='utf-8'))
file_name = 'D:/new_co/node_data.txt'
side_file = 'D:/new_co/links.txt'
data = []
matrix = []
words = []
weight = []
links = []
for row in csv_reader:
    matrix.append(row)
count = 1
for i in range(1, len(matrix)):
    words.append(matrix[i][0])
    weight.append(matrix[i][2])
print(words)
print(weight)

for i in range(len(words)):
    id = i
    category = i
    name = words[i]
    symbolSize = math.pow(int(weight[i]), 1 / 2.83)
    node = json.dumps({'id': id, 'name': name, 'symbolSize': symbolSize, 'category': category}, ensure_ascii=False)
    data.append(node)
ms = open(file_name, 'w', encoding='utf-8')
for json_str in data:
    ms.write(json_str)
    ms.write(',')

dic = {}
num = 0
for word in words:
    dic[word] = num
    num = num + 1

wb = xlrd.open_workbook('D:/new_co/graph_co.xlsx')
sh = wb.sheet_by_name('Sheet1')

for i in range(1, 56):
    id = i - 1
    name = None
    source = dic[sh.cell(i, 0).value]
    target = dic[sh.cell(i, 1).value]
    width = math.log(int(sh.cell(i, 2).value))
    value = int(sh.cell(i, 2).value)
    lineStyle = {'width': width}
    side = json.dumps({'id': id, 'lineStyle': lineStyle, "name": name, 'source': source, 'target': target},
                      ensure_ascii=False)
    links.append(side)
ff = open(side_file, 'w', encoding='utf-8')
for side_json in links:
    ff.write(side_json)
    ff.write(',')
pyperclip.copy(json.dumps(data, ensure_ascii=False))
print(words)
# for i in range(1, 12):
#     sum = 0
#     for j in range(1, 12):
#         sum = sum + int(matrix[i][j])
#     weight.append(sum)
# print(len(weight))
# print(len(words))
# dataframe = pd.DataFrame({'Id': words, 'Label': words, 'Weight': weight})
#
# dataframe.to_csv("D:/6_co_label.csv", index=False)
