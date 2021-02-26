# coding=utf-8
import json
import sys
import collections
import tomotopy as tp
from gensim import *
import gensim
# 由于文件中有多行，直接读取会出现错误，因此一行一行读取
from gensim import corpora

file = open("D:/topic_6.txt", 'r', encoding='utf-8')
papers = []
for line in file.readlines():
    papers.append(line.strip().split(' '))
# list1 = []
# list3 = []
# list5 = []
# list6 = []
# list17 = []
# list21 = []
# list8 = []
# list11 = []
# list12 = []
# list14 = []
# list19 = []
# list23 = []
# list27 = []
# list30 = []
# print(len(papers))
# print(papers[0]["seg"])
# seg = []
# for paper in papers:
#     seg.append(paper["seg"])

#     i = 0
#     if topics[0] > 0.25:
#         list1.append(paper)
#     if topics[2] > 0.25:
#         list3.append(paper)
#     if topics[4] > 0.25:
#         list5.append(paper)
#     if topics[5] > 0.25:
#         list6.append(paper)
#     if topics[16] > 0.25:
#         list17.append(paper)
#     if topics[20] > 0.25:
#         list21.append(paper)
#     if topics[7] > 0.25:
#         list8.append(paper)
#     if topics[10] > 0.25:
#         list11.append(paper)
#     if topics[11] > 0.25:
#         list12.append(paper)
#     if topics[13] > 0.25:
#         list14.append(paper)
#     if topics[18] > 0.25:
#         list19.append(paper)
#     if topics[22] > 0.25:
#         list23.append(paper)
#     if topics[26] > 0.25:
#         list27.append(paper)
#     if topics[29] > 0.25:
#         list30.append(paper)
#
# list_one = list1 + list3 + list5 + list6 + list17 + list21
# list_four = list8 + list11 + list12 + list14 + list19 + list23 + list27 + list30
#
# list_one_seg = []
# list_four_seg = []
#
# for i in list_one:
#     list_one_seg.append(i["seg"])
# for j in list_four:
#     list_four_seg.append(j["seg"])


# def read_json_lines(file_path):
#     with open(file_path, "r", encoding="utf-8")as input_file:
#         line = input_file.readline()
#         records = []
#         while line is not None and len(line) > 2:
#             records.append(json.loads(line))
#             line = input_file.readline()
#         return records
#
#
# records = read_json_lines("D:/records_with_topics.json")
# main_topic_1 = [record for record in records if
#                 record["topics"][0] > 0.25 or
#                 record["topics"][2] > 0.25 or
#                 record["topics"][4] > 0.25 or
#                 record["topics"][5] > 0.25 or
#                 record["topics"][16] > 0.25 or
#                 record["topics"][20] > 0.25 ]
#
#
# counter = 0
# with open("D:/topic_4.seg", "w", encoding="utf-8")as outfile:
#     for record in main_topic_1:
#         seg = record["seg"]
#         for word in seg:
#             outfile.write(word)
#             outfile.write(" ")
#         outfile.write("\n")
#         counter += 1
#         print(counter)
# print()

#
list_one_new = []


# with open('D:/topic_1.seg', encoding='utf-8') as f:
#     list_one = f.readlines()
# for i in list_one:
#     list_one_new.append(i.strip().split(' '))
# print(list_one_new)

# list_four_word=[]
# for i in list_four_seg:
#     for j in range(len(i)):
#         list_four_word.append(i[j])

# print(list_one_word)
# word_counts = collections.Counter(list_four_word)  # 对分词做词频统计
# word_counts_top50 = word_counts.most_common(50)  # 获取前1000最高频的词
# print(word_counts_top50)
# file = open("D:/wuhan_stop.txt", 'r')
# wuhan = file.read()
# wuhan_stop = wuhan.split(" ")
# print(wuhan_stop)
def containenglish(str0):
    import re
    return bool(re.search('[a-z]', str0))


# bianlianming
# for i in seg:
#     for j in i:
#         if containenglish(j):
#             print("删除")
#             i.remove(j)

# stop_list = ['一位', '一定', '一名', '一次', '一天', '一场', '一种', '一件', '一些']
# for i in seg:
#     for j in i:
#         if j in stop_list:
#             i.remove(j)


#
# for i in seg:
#     for j in i:
#         if j in wuhan_stop:
#             i.remove(j)


def hdp_example(a, save_path):
    mdl = tp.HDPModel(tw=tp.TermWeight.ONE, min_cf=3, rm_top=3)
    for line in a:
        mdl.add_doc(line)
    mdl.burn_in = 100
    mdl.train(0)
    print('Num docs:', len(mdl.docs), ', Vocab size:', len(mdl.used_vocabs), ', Num words:', mdl.num_words)
    print('Removed top words:', mdl.removed_top_words)
    print('Training...', file=sys.stderr, flush=True)
    number = 0
    likehood = []
    topic_number = []
    for i in range(0, 1000, 10):
        number = number + 1
        mdl.train(10)
        likehood.append(mdl.ll_per_word)
        topic_number.append(mdl.live_k)
        if number > 1 and abs(likehood[number - 1] - likehood[number - 2]) < 0.01 and topic_number[number - 1] == \
                topic_number[number - 2]:
            break
        print('likehood: {}\ttopic_number: {}'.format(likehood, topic_number))
        print('Iteration: {}\tLog-likelihood: {}\tNum. of topics: {}'.format(i, mdl.ll_per_word, mdl.live_k))
    mdl.summary()
    print('Saving...', file=sys.stderr, flush=True)
    mdl.save(save_path, True)

    important_topics = [k for k, v in sorted(enumerate(mdl.get_count_by_topics()), key=lambda x: x[1], reverse=True)]
    for k in important_topics:
        if not mdl.is_live_topic(k): continue
        print('Topic #{}'.format(k))
        for word, prob in mdl.get_topic_words(k):
            print('\t', word, prob, sep='\t')


def lda_example(a, save_path):
    mdl = tp.LDAModel(tw=tp.TermWeight.ONE, min_cf=3, rm_top=3, k=14)
    for line in a:
        mdl.add_doc(line)
    mdl.burn_in = 100
    mdl.train(0)
    print('Num docs:', len(mdl.docs), ', Vocab size:', len(mdl.used_vocabs), ', Num words:', mdl.num_words)
    print('Removed top words:', mdl.removed_top_words)
    print('Training...', file=sys.stderr, flush=True)
    for i in range(0, 1000, 10):
        mdl.train(10)
        print('Iteration: {}\tLog-likelihood: {}'.format(i, mdl.ll_per_word))
    mdl.summary()
    print('Saving...', file=sys.stderr, flush=True)
    mdl.save(save_path, True)
    for k in range(mdl.k):
        print(mdl.get_topic_words(k, top_n=50))
    # for k in range(mdl.k):
    #     print(mdl.get_count_by_topics())


print('Running LDA')
lda_example(papers, 'D:/test.lda.bin_new')
# print(papers[0])
# print('Running HDP')
# hdp_example(papers, 'D:/test.hdp.bin')
# hdp_example(list_four_seg, 'E:/test.hdp.bin')

# print(list1)

"""构建词频矩阵，训练LDA模型"""
# dictionary = corpora.Dictionary(list_one_seg)
# dictionary2 = corpora.Dictionary(list_four_new)
# corpus[0]: [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1),...]
# corpus是把每条新闻ID化后的结果，每个元素是新闻中的每个词语，在字典中的ID和频率
# corpus = [dictionary.doc2bow(text) for text in list_one_seg]
#
# corpus2 = [dictionary.doc2bow(text) for text in list_four_new]
#
# lda = models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=4)
# topic_list = lda.print_topics(4)
# print("4个主题的单词分布为：\n")
# for topic in topic_list:
#     print(topic)
#
#
# lda2 = models.LdaModel(corpus=corpus2, id2word=dictionary2, num_topics=20)
# topic_list2 = lda2.print_topics(4)
# print("4个主题的单词分布为：\n")
# for topic in topic_list2:
#     print(topic)
# print(lda2.print_topics(num_topics=20, num_words=20))
