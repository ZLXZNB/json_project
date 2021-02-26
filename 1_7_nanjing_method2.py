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


file_result = 'D:/second_method_data.xlsx'
workbook_result = xlsxwriter.Workbook(file_result)
worksheet_result = workbook_result.add_worksheet('Sheet1')

list_only = [0] * 11

# file = open("D:/final_result.json", 'r', encoding='utf-8')
# line = file.readline()
file = open("D:/final_result.json", 'r', encoding='utf-8')
line = file.readline()
content_all = []
number = 0
number_list = [0 for x in range(0, 14)]
index_list = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']

with open('D:/line-smooth.html') as file_obj:
    html_string = file_obj.read()

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
line_dict_list = []
while line:
    category = []
    dic = json.loads(line)
    line_dict = {}
    publish_time = dic["publish_time"]
    topic = dic["topic_main"]
    topic_6 = dic["topic_6"]
    if publish_time < "2020-06-01":
        if topic[26] > 0.25:
            topic_nine_dic.append(dic)
            print("已成功加入")
            category.append(labels[8])
        if topic[1] > 0.25 or topic[14] > 0.25 or topic[33] > 0.25:
            topic_seven_dic.append(dic)
            print("已成功加入")
            category.append(labels[6])
        if topic[12] > 0.25 or topic[20] > 0.25 or topic[28] > 0.25:
            topic_three_dic.append(dic)
            print("已成功加入")
            category.append(labels[2])
        if topic[4] > 0.25 or topic[6] > 0.25 or topic[27] > 0.25 or topic[22] > 0.25 or topic[31] > 0.25 or topic[
            32] > 0.25:
            topic_two_dic.append(dic)
            print("已成功加入")
            category.append(labels[1])
        if topic[24] > 0.25 or topic[35] > 0.25 or topic[18] > 0.25 or topic[25] > 0.25 or topic[8] > 0.25:
            topic_one_dic.append(dic)
            print("已成功加入")
            category.append(labels[0])
        if topic[0] > 0.25 or topic[15] > 0.25 or topic[16] > 0.25 or topic[3] > 0.25 or topic[29] > 0.25:
            topic_six_dic.append(dic)
            print("已成功加入")
            category.append(labels[5])
        if topic[9] > 0.25 or topic[13] > 0.25 or topic[36] > 0.25 or topic[10] > 0.25 or topic[2] > 0.25 or topic[
            34] > 0.25:
            topic_four_dic.append(dic)
            print("已成功加入")
            category.append(labels[3])
        if topic[19] > 0.25 or topic[21] > 0.25 or topic[7] > 0.25:
            topic_five_dic.append(dic)
            print("已成功加入")
            category.append(labels[4])
        if (topic_6[0] > 0.25 or topic_6[10] > 0.25 or topic_6[1] > 0.25 or topic_6[2] > 0.25 or topic_6[8] > 0.25 or
            topic_6[7]
            > 0.25 or topic_6[6] > 0.25 or topic_6[12] > 0.25 or topic_6[5] > 0.25) and topic[5] > 0.25:
            topic_ten_dic.append(dic)
            print("已成功加入")
            category.append(labels[9])
        if topic[23] > 0.25 or topic[30] > 0.25:
            topic_eight_dic.append(dic)
            print("已成功加入")
            category.append(labels[7])
        probability_list = [0] * 10
        probability_list[0] = topic[24] + topic[35] + topic[18] + topic[25] + topic[8]
        probability_list[1] = topic[4] + topic[6] + topic[27] + topic[22] + topic[31] + topic[32]
        probability_list[2] = topic[12] + topic[20] + topic[28]
        probability_list[3] = topic[9] + topic[13] + topic[36] + topic[10] + topic[2] + topic[34]
        probability_list[4] = topic[19] + topic[21] + topic[7]
        probability_list[5] = topic[0] + topic[15] + topic[16] + topic[3] + topic[29]
        probability_list[6] = topic[1] + topic[14] + topic[33]
        probability_list[7] = topic[23] + topic[30]
        probability_list[8] = topic[26]
        probability_list[9] = topic[5] * (topic_6[0] + topic_6[10] + topic_6[1] + topic_6[2] + topic_6[8] + topic_6[7] +
                                          topic_6[6] + topic_6[12] + topic_6[5])

    line_dict = {"labels": category, "publish_time": publish_time, "probability_list": probability_list}
    line_dict_list.append(line_dict)
    line = file.readline()

all_list = [topic_one_dic, topic_two_dic, topic_three_dic, topic_four_dic, topic_five_dic, topic_six_dic,
            topic_seven_dic, topic_eight_dic, topic_nine_dic, topic_ten_dic]


def get_timestamp(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d").timestamp()


def get_all_time(total_list):
    total_time_dictionary = {}
    for dictionary_list_first in total_list:
        for dictionary in dictionary_list_first:
            if dictionary['publish_time'] in total_time_dictionary:
                total_time_dictionary[dictionary["publish_time"]] += 1
            else:
                total_time_dictionary[dictionary["publish_time"]] = 1
    time_list_first = list(total_time_dictionary.keys())
    date_list_first = sorted(time_list_first, key=lambda time: get_timestamp(time))
    return date_list_first


def draw_graph_by_time(total_list):
    series = []
    for i in range(len(total_list)):
        time_dictionary = {}
        for dictionary in total_list[i]:
            if dictionary["publish_time"] in time_dictionary:
                time_dictionary[dictionary["publish_time"]] += 1
            else:
                time_dictionary[dictionary["publish_time"]] = 1
        series.append(time_dictionary)
    return series


def get_value(pending_list, position):
    if position < len(pending_list):
        return pending_list[position]
    else:
        return 0


def get_dictionary_value(index, dictionary_of):
    if index not in dictionary_of.keys():
        return 0
    if index in dictionary_of.keys():
        return dictionary_of[index]


result_list = draw_graph_by_time(all_list)
print("获取所有主体数据完成")
all_date_list = get_all_time(all_list)
print("获取所有时间完成")
final_result_list = []
for i in range(len(result_list)):
    for j in range(i + 1, 10):
        data_co = []
        co_dictionary = {}
        # for dictionary in all_list[i]:
        #     if dictionary in all_list[j]:

        for line in line_dict_list:
            if line["publish_time"] not in co_dictionary:
                co_dictionary[line["publish_time"]] = line["probability_list"][i]*line["probability_list"][j]
            else:
                co_dictionary[line["publish_time"]] += line["probability_list"][i]*line["probability_list"][j]

        co_dictionary_number = {}
        for line in line_dict_list:
            if labels[i] in line["labels"] and labels[j] in line["labels"]:
                if line["publish_time"] not in co_dictionary_number:
                    co_dictionary_number[line["publish_time"]] = 1
                else:
                    co_dictionary_number[line["publish_time"]] += 1
        print("获取两个主题之间的共现数据完成")
        for date in all_date_list:
            if get_dictionary_value(date, result_list[i]) + get_dictionary_value(date,
                                                                                 result_list[j]) - get_dictionary_value(
                date, co_dictionary_number) == 0:
                data_co.append(0)
            else:
                data_co.append(get_dictionary_value(date, co_dictionary) / (
                        get_dictionary_value(date, result_list[i]) + get_dictionary_value(date, result_list[
                    j]) - get_dictionary_value(date, co_dictionary_number)))
        option = {"title": {"text": labels[i] + "和" + labels[j]}, "xAxis": {"type": 'category', "data": all_date_list},
                  "yAxis": {"type": 'value'}, "series": [{"data": data_co, "type": 'line', "smooth": 'true'}]}


        final_string = html_string.replace("#{placeholder}", json.dumps(option))
        name_of_content = labels[i] + "和" + labels[j]
        file_name = "D:/1_7_nanjing_method_2/" + name_of_content + ".html"
        with open(file_name, 'w') as f:
            f.write(final_string)
        final_result_list.append(option)
        print(i)
        print(j)
        print("完成")
# pyperclip.copy(json.dumps(final_result_list, ensure_ascii=False))
# result_list = draw_graph_by_time(all_list)
# result_data = []
# for result in result_list:
#     result_data.append(result["data"])
#
# final_result_data = []
# for data in result_data:
#     replaced_data = []
#     for i in range(len(data)):
#         total_portion = 0
#         for j in range(len(result_data)):
#             total_portion = total_portion + get_value(result_data[j], i)
#         replaced_data.append(data[i] / total_portion)
#     final_result_data.append(replaced_data)
#
# final_result_list = []
# for i in range(len(result_list)):
#     final_result_list.append(
#         {"name": labels[i], "type": "line", "stack": "总量", "areaStyle": {}, "data": final_result_data[i],
#          "symbol": 'none', "smooth": True})
# pyperclip.copy(json.dumps(final_result_list, ensure_ascii=False))
