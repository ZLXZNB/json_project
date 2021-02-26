import json
import codecs
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim import corpora, models
import tomotopy as tp

# file = open("D:/final_result.json", 'r', encoding='utf-8')
# line = file.readline()
file_record = open("D:/records.json", 'r', encoding='utf-8')
line = file_record.readline()
source_all = []
number = 0
while line:
    number = number + 1
    dic = json.loads(line)
    print(number)
    source_all.append(dic["source"])
    line = file_record.readline()
source = set(source_all)

for element in source:
    file = open("D:/records.json", 'r', encoding='utf-8')
    line = file.readline()
    publish_time_all = []
    number = 0
    while line:
        number = number + 1
        dic = json.loads(line)
        source = dic["source"]
        print(number)
        if source == element:
            print("找到")
            publish_time_all.append(dic["publish_time"])
        line = file.readline()
    time = sorted(set(publish_time_all))
    numbers = []
    for time_stap in time:
        number_new = 0
        for time_all in publish_time_all:
            if time_all == time_stap:
                number_new = number_new + 1
        numbers.append(number_new)
    final_result = list(zip(time, numbers))
    title_file_name = r"D:/source/" + element + ".txt"
    ms = open(title_file_name, 'w', encoding='utf-8')
    for key in final_result:
        ms.write(str(key))
        ms.write('\n')
    print('写入完成')
    file.close()

# numbers = []
# for source_single in source:
#     number_new = 0
#     for single_source in source_all:
#         if single_source == source_single:
#             number_new = number_new+1
#     numbers.append(number_new)
# final_result = list(zip(source, numbers))
# title_file_name = 'D:/source.txt'
# ms = open(title_file_name, 'w', encoding='utf-8')
# for element in final_result:
#     ms.write(str(element))
#     ms.write('\n')
# print('写入完成')
# file.close()
