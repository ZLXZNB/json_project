import json
import xlsxwriter
import codecs
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim import corpora, models


def get_str(word_list):
    str_words = ''
    for j in range(len(word_list)):
        if j < len(word_list) - 1:
            str_words = str_words + word_list[j] + ';'
        if j == len(word_list) - 1:
            str_words = str_words + word_list[j]
    return str_words


def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))


file_1 = 'D:/12_25_topic_co/01-19_02-20.xlsx'
workbook = xlsxwriter.Workbook(file_1)
worksheet = workbook.add_worksheet('Sheet1')

file_2 = 'D:/12_25_topic_co/02-20_03-17.xlsx'
workbook_2 = xlsxwriter.Workbook(file_2)
worksheet_2 = workbook_2.add_worksheet('Sheet1')

file_3 = 'D:/12_25_topic_co/03-17_04-26.xlsx'
workbook_3 = xlsxwriter.Workbook(file_3)
worksheet_3 = workbook_3.add_worksheet('Sheet1')

file_4 = 'D:/12_25_topic_co/all_time.xlsx'
workbook_4 = xlsxwriter.Workbook(file_4)
worksheet_4 = workbook_4.add_worksheet('Sheet1')

list_only = [0] * 11

# file = open("D:/final_result.json", 'r', encoding='utf-8')
# line = file.readline()
file = open("D:/final_result.json", 'r', encoding='utf-8')
line = file.readline()
content_all = []
number = 0
number_list = [0 for x in range(0, 14)]
index_list = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
labels = ['疫情中的众生相', '防控部署', '医疗物资保障与基础设施建设', '疫情中的经济', '疫情中的文化传播', '疫情中的民生', '新冠肺炎医治', '疫情中的国际社会', '新冠疫情动态', '疫情中的法制']
color_list = ["#567C73", "#9ed566", "#2BCC7F", "#809B48", "#9B2D1F", "#604878", "#A5644E", "#2D3F3A",
              "#761721"]
null_number = 0
dict_first = {}
count_map = {"none": {}}
for i in range(10):
    dic_two = {}
    for j in range(i + 1, 10):
        dic_two[labels[j]] = 0
    dict_first[labels[i]] = dic_two
one_number = 0
two_number = 0
self_co = [0] * 10
while line:
    category = []
    dic = json.loads(line)
    publish_time = dic["publish_time"]
    if "2020-03-17" < publish_time < "2020-04-26":
        topic = dic["topic_main"]
        topic_6 = dic["topic_6"]
        if topic[26] > 0.25:
            category.append('新冠疫情动态')
        if topic[1] > 0.25 or topic[14] > 0.25 or topic[33] > 0.25:
            category.append('新冠肺炎医治')
        if topic[12] > 0.25 or topic[20] > 0.25 or topic[28] > 0.25:
            category.append('医疗物资保障与基础设施建设')
        # if topic[11] > 0.25 or topic[17] > 0.25:
        #     category.append('四')
        if topic[4] > 0.25 or topic[6] > 0.25 or topic[27] > 0.25 or topic[22] > 0.25 or topic[31] > 0.25 or topic[
            32] > 0.25:
            category.append('防控部署')
        if topic[24] > 0.25 or topic[35] > 0.25 or topic[18] > 0.25 or topic[25] > 0.25 or topic[8] > 0.25:
            category.append('疫情中的众生相')
        if topic[0] > 0.25 or topic[15] > 0.25 or topic[16] > 0.25 or topic[3] > 0.25 or topic[29] > 0.25:
            category.append('疫情中的民生')
        if topic[9] > 0.25 or topic[13] > 0.25 or topic[36] > 0.25 or topic[10] > 0.25 or topic[2] > 0.25 or topic[
            34] > 0.25:
            category.append('疫情中的经济')
        if topic[19] > 0.25 or topic[21] > 0.25 or topic[7] > 0.25:
            category.append('疫情中的文化传播')
        if (topic_6[0] > 0.25 or topic_6[10] > 0.25 or topic_6[1] > 0.25 or topic_6[2] > 0.25 or topic_6[8] > 0.25 or
            topic_6[7]
            > 0.25 or topic_6[6] > 0.25 or topic_6[12] > 0.25 or topic_6[5] > 0.25) and topic[5] > 0.25:
            category.append('疫情中的法制')
        if topic[23] > 0.25 or topic[30] > 0.25:
            category.append('疫情中的国际社会')
        for i in range(10):
            if labels[i] in category:
                self_co[i] += 1
        for i in range(10):
            for j in range(i + 1, 10):
                if labels[i] in category and labels[j] in category:
                    print('匹配成功')
                    dict_first[labels[i]][labels[j]] += 1
    line = file.readline()
print("dict")
print(dict_first)
# for i in range(10):
#     worksheet_3.write(i + 1, i + 1, self_co[i] / self_co[i])
#     for j in range(i + 1, 10):
#         worksheet_3.write(i + 1, j + 1, dict_first[labels[i]][labels[j]] / self_co[i])
#     for m in range(1, i + 1):
#         worksheet_3.write(i + 1, m, dict_first[labels[m - 1]][labels[i]] / self_co[i])
# workbook_3.close()
top_5_label = []
topic_dictionary = {}
for i in range(len(self_co)):
    topic_dictionary[labels[i]] = self_co[i]
sorted_topic_dictionary = sort_dict_by_value(topic_dictionary)
print("sorted_topic_dictionary")
print(sorted_topic_dictionary)
sorted_topic = list(sorted_topic_dictionary.keys())
print("sorted_topic")
print(sorted_topic)
for i in range(5):
    top_5_label.append(sorted_topic[i])
print("后5的类别为")
print(top_5_label)
for i in range(len(top_5_label)):
    keys_all = list(sorted_topic_dictionary.keys())
    needed_labels = []
    for key in keys_all:
        if key != top_5_label[i]:
            needed_labels.append(key)
    data = [{"name": top_5_label[i], "value": sorted_topic_dictionary[top_5_label[i]],
             "itemStyle": {"normal": {"color": "#D13438"}}}]
    for j in range(len(needed_labels)):
        data.append({"name": needed_labels[j], "itemStyle": {"normal": {"color": color_list[j]}}})
    links = []
    for label in needed_labels:
        if label in dict_first[top_5_label[i]].keys():
            value = dict_first[top_5_label[i]][label]
        else:
            value = dict_first[label][top_5_label[i]]
        links.append({"source": top_5_label[i], "target": label, "value": value})
    option = {
        "series": {"type": 'sankey', "layout": 'none', "focusNodeAdjacency": 'allEdges', "data": data,
                   "links": links,
                   "lineStyle": {"color": "target"
                                 }}}
    print(i)
    print("option")
    print(option)
for i in range(10):
    worksheet_3.write(i + 1, 0, labels[i])
    worksheet_3.write(0, i + 1, labels[i])
    worksheet_3.write(i + 1, i + 1, 1)
    for j in range(i + 1, 10):
        worksheet_3.write(i + 1, j + 1, dict_first[labels[i]][labels[j]] / self_co[i])
    for m in range(1, i + 1):
        worksheet_3.write(i + 1, m, dict_first[labels[m - 1]][labels[i]] / self_co[i])
workbook_3.close()

#
#     for i in range(11):
#         if category == [index_list[i]]:
#             list_only[i] = list_only[i] + 1
#
#     if len(category) == 1:
#         topic = category[0]
#         if topic not in count_map["none"]:
#             count_map["none"][topic] = 1
#         else:
#             count_map["none"][topic] += 1
#
#     for topic in category:
#         if topic not in count_map:
#             count_map[topic] = {}
#
#         for another in category:
#             if another in count_map[topic]:
#                 count_map[topic][another] += 1
#             else:
#                 count_map[topic][another] = 1
#
#     if category:
#         number = number + 1
#         worksheet.write(number - 1, 0, get_str(category))
#     line = file.readline()
# workbook.close()
# print(count_map)
# print(dict)

# for i in range(11):
#     worksheet_2.write(i + 1, 12, list_only[i])
#     worksheet_2.write(i + 1, 0, index_list[i])
#     worksheet_2.write(0, i + 1, index_list[i])
# workbook_2.close()
