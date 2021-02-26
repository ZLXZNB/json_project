import json
import xlsxwriter
import codecs
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim import corpora, models

file_li = open("D:/liwenliang.txt", 'a', encoding='utf-8')
# file = open("D:/final_result.json", 'r', encoding='utf-8')
# line = file.readline()
file = open("D:/final_result.json", 'r', encoding='utf-8')
line = file.readline()
li_number = 0
number = 0
probability = []
counter = 0
while line:
    number = number + 1
    dic = json.loads(line)
    topic = dic["topic_6"]
    content = dic["seg"]
    # print(number)
    if '李文亮' in content and topic[10] > 0.25:
        print(topic[10])
        # probability.append(topic[10])
        counter += 1
    # if topic[10] > 0.25:
    #     if '李文亮' in content:
    #         probability.append(topic[10])
    #
    #         li_number = li_number+1
    #     for word in content:
    #         file_li.write(word)
    #         file_li.write(' ')
    #     file_li.write('\n')
    line = file.readline()

print(counter)
# print(probability)
# quater = 0
# for content in probability:
#     if content > 0.25:
#         quater = quater+1
# print(quater/len(probability))
