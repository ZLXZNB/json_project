# coding=utf-8
import json
import sys
import collections
import tomotopy as tp
from gensim import *
import gensim
# 由于文件中有多行，直接读取会出现错误，因此一行一行读取
from gensim import corpora

file = open("D:/final_result.json", 'r', encoding='utf-8')
file_full = open("D:/dbnews.covid_wuhan_news.json", 'r', encoding='utf-8')
probility_1 = open("D:/20_topic/1.txt", 'a', encoding='utf-8')
probility_2 = open("D:/20_topic/2.txt", 'a', encoding='utf-8')
probility_3 = open("D:/20_topic/3.txt", 'a', encoding='utf-8')
title_1 = []
title_2 = []
title_3 = []
number = 0
line = file.readline()
while line:
    number = number + 1
    dic = json.loads(line)
    topic = dic["topic_main"]
    content = dic["seg"]
    title = dic["title"]
    print(number)
    if 0.24 < topic[19] < 0.26:
        title_1.append(title)
    if 0.475 < topic[19] < 0.525:
        title_2.append(title)
    if topic[19] > 0.85:
        title_3.append(title)
    line = file.readline()

number_double = 0
line_full = file_full.readline()
while line_full:
    number_double += 1
    print(number_double)
    dic = json.loads(line_full)
    title = dic["tt"]
    content = dic["ct"]
    if title in title_1 and content is not None:
        probility_1.write(content)
        probility_1.write('\n')
        print("写入")
    if title in title_2 and content is not None:
        probility_2.write(content)
        probility_2.write('\n')
        print("写入")
    if title in title_3 and content is not None:
        probility_3.write(content)
        probility_3.write('\n')
        print("写入")
    line_full = file_full.readline()

probility_1.close()
probility_2.close()
probility_3.close()
