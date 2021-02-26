import json
import codecs
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim import corpora, models
import tomotopy as tp

file = open("D:/seg2020.txt", 'r', encoding='utf-8')
file_en = open("D:/with_topics.txt", 'r', encoding='utf-8')
model_6 = tp.LDAModel.load('D:/test.lda.bin_new')
model_main = tp.LDAModel.load('D:/model/lda_final')
ms = open('D:/final_result.json', 'w', encoding='utf-8')

line = file.readline()
line_en = file_en.readline()
number = 0

while line and line_en:
    number = number + 1
    line_list = line.strip().split(' ')
    doc_inst_6 = model_6.make_doc(line_list)
    topic_dist_6, ll_6 = model_6.infer(doc_inst_6, iter=25)

    doc_inst_main = model_main.make_doc(line_list)
    topic_dist_main, ll_main = model_main.infer(doc_inst_main, iter=25)

    dic = json.loads(line_en)

    seg = line_list
    publish_time = dic["publish_time"]
    source = dic["source"]
    title = dic["title"]
    data = json.dumps({'seg': seg, 'publish_time': publish_time, 'source': source, 'title': title,
                       'topic_main': topic_dist_main.tolist(), 'topic_6': topic_dist_6.tolist()})
    ms.write(data)
    ms.write('\n')
    line = file.readline()
    line_en = file_en.readline()
    print(number)

# papers = []
# for line in open("D:/seg2020.txt", 'r', encoding='utf-8'):
#     papers.append(line.strip().split(' '))
# paper_en = []
#
# for line in open("D:/with_topics.txt", 'r', encoding='utf-8'):
#     dic = json.loads(line)
#     paper_en.append(dic)
# for line in file.readlines():
#     dic = json.loads(line)
#     papers.append(dic)
# print(len(papers))
# print(papers[0]["seg"])
# content = []
# for paper in papers:
#     content.append(paper["seg"])
# print(len(content))

# lda = models.ldamodel.LdaModel.load('D:/model/lda_model_1')
# model_1 = tp.LDAModel.load('D:/model/lda_model_1')
# model_4 = tp.LDAModel.load('D:/model/lda_model_4')
# model_6 = tp.LDAModel.load('D:/test.lda.bin_new')
# model_main = tp.LDAModel.load('D:/model/lda_final')
#
# ms = open('D:/final_result.json', 'w', encoding='utf-8')
# file_3 = open('D:/topic_6/3.txt', 'w', encoding='utf-8')
# file_5 = open('D:/topic_6/5.txt', 'w', encoding='utf-8')
# file_9 = open('D:/topic_6/9.txt', 'w', encoding='utf-8')
# file_12 = open('D:/topic_6/12.txt', 'w', encoding='utf-8')
# file_13 = open('D:/topic_6/13.txt', 'w', encoding='utf-8')
# for i in range(len(papers)):
#     doc_inst = model_final.make_doc(papers[i])
#     topic_dist, ll = model_final.infer(doc_inst)
#     if topic_dist[2] > 0.5:
#         for word in papers[i]:
#             file_3.write(word)
#             file_3.write(' ')
#         file_3.write('\n')
#         print(i)
#         print("主题3写入")
#     if topic_dist[4] > 0.5:
#         for word in papers[i]:
#             file_5.write(word)
#             file_5.write(' ')
#         file_5.write('\n')
#         print(i)
#         print("主题5写入")
#     if topic_dist[8] > 0.5:
#         for word in papers[i]:
#             file_9.write(word)
#             file_9.write(' ')
#         file_9.write('\n')
#         print(i)
#         print("主题9写入")
#     if topic_dist[11] > 0.5:
#         for word in papers[i]:
#             file_12.write(word)
#             file_12.write(' ')
#         file_12.write('\n')
#         print(i)
#         print("主题12写入")
#     if topic_dist[12] > 0.5:
#         for word in papers[i]:
#             file_13.write(word)
#             file_13.write(' ')
#         file_13.write('\n')
#         print(i)
#         print("主题13写入")
# print(len(papers))
# for i in range(len(papers)):
#     doc_inst_6 = model_6.make_doc(papers[i])
#     topic_dist_6, ll_6 = model_6.infer(doc_inst_6)
#
#     doc_inst_main = model_main.make_doc(papers[i])
#     topic_dist_main, ll_main = model_main.infer(doc_inst_main)
#
#     seg = papers[i]
#     publish_time = paper_en[i]["publish_time"]
#     source = paper_en[i]["source"]
#     title = paper_en[i]["title"]
#     data = json.dumps({'seg': seg, 'publish_time': publish_time, 'source': source, 'title': title,
#                        'topic_main': topic_dist_main.tolist(), 'topic_6': topic_dist_6.tolist()})
#
#     ms.write(data)
#     ms.write('\n')
#     print(i)
