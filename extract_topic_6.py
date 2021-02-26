# coding=utf-8
import json
import sys
import collections
import tomotopy as tp
from gensim import *
import gensim
# 由于文件中有多行，直接读取会出现错误，因此一行一行读取
from gensim import corpora

file = open("D:/with_topics.txt", 'r', encoding='utf-8')
file2 = open('D:/topic_6.txt', 'w', encoding='utf-8')
file3 = open("D:/seg2020.txt", 'r', encoding='utf-8')

topic_str = []
for line in file3.readlines():
    topic_str.append(line)

line_number = 0
for line in file.readlines():
    line_number = line_number + 1
    dic = json.loads(line)
    if dic["topics"][5] > 0.3:
        file2.write(topic_str[line_number - 1])
        print(line_number)
        print("写入")

