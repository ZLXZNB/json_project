import json
import xlsxwriter
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from matplotlib.pyplot import rcParams
import pyperclip


def get_str(word_list):
    str_words = ''
    for j in range(len(word_list)):
        if j < len(word_list) - 1:
            str_words = str_words + word_list[j] + ';'
        if j == len(word_list) - 1:
            str_words = str_words + word_list[j]
    return str_words


file_1 = 'D:/12_25_topic_co/01-19_02-20.xlsx'
workbook = xlsxwriter.Workbook(file_1)
worksheet = workbook.add_worksheet('Sheet1')

file_2 = 'D:/12_25_topic_co/02-20_03-17.xlsx'
workbook_2 = xlsxwriter.Workbook(file_2)
worksheet_2 = workbook_2.add_worksheet('Sheet1')

file_3 = 'D:/12_25_topic_co/03-17_04-26.xlsx'
workbook_3 = xlsxwriter.Workbook(file_3)
worksheet_3 = workbook_3.add_worksheet('Sheet1')

list_only = [0] * 11

# file = open("D:/final_result.json", 'r', encoding='utf-8')
# line = file.readline()
file = open("D:/final_result.json", 'r', encoding='utf-8')
line = file.readline()
content_all = []
number = 0
number_list = [0 for x in range(0, 14)]
index_list = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']

topic_one_dic = []
topic_two_dic = []
topic_three_dic = []
topic_four_dic = []
topic_five_dic = []
topic_six_dic = []
topic_seven_dic = []
topic_eight_dic = []
topic_nine_dic = []
topic_ten_dic = []
labels = ['疫情中的众生相', '防控部署', '医疗物资保障与基础设施建设', '疫情中的经济', '疫情中的文化传播', '疫情中的民生', '新冠肺炎医治', '疫情中的国际社会', '新冠疫情动态', '疫情中的法制']
null_number = 0
one_number = 0
two_number = 0
self_co = [0] * 10
while line:
    category = []
    dic = json.loads(line)
    publish_time = dic["publish_time"]
    topic = dic["topic_main"]
    topic_6 = dic["topic_6"]
    if topic[26] > 0.25:
        topic_nine_dic.append(dic)
        print("已成功加入")
    if topic[1] > 0.25 or topic[14] > 0.25 or topic[33] > 0.25:
        topic_seven_dic.append(dic)
        print("已成功加入")
    if topic[12] > 0.25 or topic[20] > 0.25 or topic[28] > 0.25:
        topic_three_dic.append(dic)
        print("已成功加入")
    if topic[4] > 0.25 or topic[6] > 0.25 or topic[27] > 0.25 or topic[22] > 0.25 or topic[31] > 0.25 or topic[
        32] > 0.25:
        topic_two_dic.append(dic)
        print("已成功加入")
    if topic[24] > 0.25 or topic[35] > 0.25 or topic[18] > 0.25 or topic[25] > 0.25 or topic[8] > 0.25:
        topic_one_dic.append(dic)
        print("已成功加入")
    if topic[0] > 0.25 or topic[15] > 0.25 or topic[16] > 0.25 or topic[3] > 0.25 or topic[29] > 0.25:
        topic_six_dic.append(dic)
        print("已成功加入")
    if topic[9] > 0.25 or topic[13] > 0.25 or topic[36] > 0.25 or topic[10] > 0.25 or topic[2] > 0.25 or topic[
        34] > 0.25:
        topic_four_dic.append(dic)
        print("已成功加入")
    if topic[19] > 0.25 or topic[21] > 0.25 or topic[7] > 0.25:
        topic_five_dic.append(dic)
        print("已成功加入")
    if (topic_6[0] > 0.25 or topic_6[10] > 0.25 or topic_6[1] > 0.25 or topic_6[2] > 0.25 or topic_6[8] > 0.25 or
        topic_6[7]
        > 0.25 or topic_6[6] > 0.25 or topic_6[12] > 0.25 or topic_6[5] > 0.25) and topic[5] > 0.25:
        topic_ten_dic.append(dic)
        print("已成功加入")
    if topic[23] > 0.25 or topic[30] > 0.25:
        topic_eight_dic.append(dic)
        print("已成功加入")
    line = file.readline()

all_list = [topic_one_dic, topic_two_dic, topic_three_dic, topic_four_dic, topic_five_dic, topic_six_dic,
            topic_seven_dic, topic_eight_dic, topic_nine_dic, topic_ten_dic]


def get_timestamp(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d").timestamp()


def draw_graph_by_time(total_list):
    total_time_dictionary = {}
    for dictionary_list_first in total_list:
        for dictionary in dictionary_list_first:
            if dictionary['publish_time'] in total_time_dictionary:
                total_time_dictionary[dictionary["publish_time"]] += 1
            else:
                total_time_dictionary[dictionary["publish_time"]] = 1
    time_list_first = list(total_time_dictionary.keys())
    date_list_first = sorted(time_list_first, key=lambda time: get_timestamp(time))

    series = []
    for i in range(len(total_list)):
        time_dictionary = {}
        for dictionary in total_list[i]:
            if dictionary["publish_time"] in time_dictionary:
                time_dictionary[dictionary["publish_time"]] += 1
            else:
                time_dictionary[dictionary["publish_time"]] = 1
        time_list = list(time_dictionary.keys())
        date_list = sorted(time_list, key=lambda time: get_timestamp(time))
        data = []
        for date in date_list:
            data.append(time_dictionary[date] / total_time_dictionary[date])
        topic_dictionary = {"name": labels[i], "type": "line", "data": data, "symbol": 'none', "smooth": True,
                            "stack": "总量", "areaStyle": {}}
        series.append(topic_dictionary)
    return series


def get_value(pending_list, position):
    if position < len(pending_list):
        return pending_list[position]
    else:
        return 0


result_list = draw_graph_by_time(all_list)
result_data = []
for result in result_list:
    result_data.append(result["data"])

final_result_data = []
for data in result_data:
    replaced_data = []
    for i in range(len(data)):
        total_portion = 0
        for j in range(len(result_data)):
            total_portion = total_portion + get_value(result_data[j], i)
        replaced_data.append(data[i] / total_portion)
    final_result_data.append(replaced_data)

final_result_list = []
for i in range(len(result_list)):
    final_result_list.append(
        {"name": labels[i], "type": "line", "stack": "总量", "areaStyle": {}, "data": final_result_data[i],
         "symbol": 'none', "smooth": True})
pyperclip.copy(json.dumps(final_result_list, ensure_ascii=False))
