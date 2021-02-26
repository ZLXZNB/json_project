import json
import codecs
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim import corpora, models
import tomotopy as tp

# file = open("D:/final_result.json", 'r', encoding='utf-8')
# line = file.readline()
for i in range(14):
    file = open("D:/final_result.json", 'r', encoding='utf-8')
    line = file.readline()
    publish_time_all = []
    number = 0
    while line:
        number = number + 1
        dic = json.loads(line)
        topic = dic["topic_6"]
        topic_main = dic["topic_main"]
        print(topic)
        print(len(topic))
        print(number)
        if topic[i] > 0.25 and topic_main[5] > 0.25:
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
    title_file_name = r"D:/topic_6_time/" + str(i) + ".txt"
    ms = open(title_file_name, 'w', encoding='utf-8')
    for element in final_result:
        ms.write(str(element))
        ms.write('\n')
    print('写入完成')
    file.close()
