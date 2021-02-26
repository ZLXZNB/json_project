import json
import codecs
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim import corpora, models
import tomotopy as tp
import re

file = open("D:/topic_6.txt", 'r', encoding='utf-8')
# print(file.readline())



# papers = []
# for line in file.readlines():
#     dic = json.loads(line)
#     papers.append(dic)
# print(len(papers))
# print(papers[0]["seg"])
# content = []
# for paper in papers:
#     content.append(paper["seg"])
# print(len(content))

for i in range(8, 37):
    title_file_name = r"D:/titles/" + str(i) + ".txt"
    path_name = r"D:/topic/" + "topic" + str(i) + "/"
    # title_file = open("D:/titles/8.txt", "r", encoding='utf-8')
    title_file = open(title_file_name, "r", encoding='utf-8')
    # path = r"D:/topic/topic8/"
    path = path_name
    titles = title_file.readlines()
    title_final = []
    for title in titles:
        title = title.strip()
        title_final.append(title)
    for line in open("D:/dbnews.covid_wuhan_news.json", 'r', encoding='utf-8'):
        dic = json.loads(line)
        if dic["tt"] in title_final:
            print(type(dic["tt"]))

            text_name = re.sub(r'[?\\|<>/*:\\…"]', '', dic["tt"])
            file_name = path + text_name + ".txt"
            ms = open(file_name, 'w', encoding='utf-8')
            data = dic["ct"]
            if data is not None:
                ms.write(data)
                print("写入完成")



    # line_number =0
    # print(title)
    # for line in open("D:/dbnews.covid_wuhan_news.json", 'r', encoding='utf-8'):
    #     dic = json.loads(line)
    #     line_number = line_number+1
    #     print(line_number)
    #     print(dic["tt"])
    #     if dic["tt"] == title:
    #         file_name = path + title + ".txt"
    #         ms = open(file_name, 'w', encoding='utf-8')
    #         data = dic["ct"]
    #         ms.write(data)
    #         print(line_number)
    #         print("写入完成")
    #         print(title)
    #         break
