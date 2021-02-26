import json
import xlsxwriter
import codecs
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim import corpora, models
import pyperclip


def get_str(word_list):
    str_words = ''
    for j in range(len(word_list)):
        if j < len(word_list) - 1:
            str_words = str_words + word_list[j] + ';'
        if j == len(word_list) - 1:
            str_words = str_words + word_list[j]
    return str_words


file_1 = 'D:/12_28_nanjing_co/01-19_02-20.xlsx'
workbook = xlsxwriter.Workbook(file_1)
worksheet = workbook.add_worksheet('Sheet1')

file_2 = 'D:/12_28_nanjing_co/02-20_03-17.xlsx'
workbook_2 = xlsxwriter.Workbook(file_2)
worksheet_2 = workbook_2.add_worksheet('Sheet1')

file_3 = 'D:/12_28_nanjing_co/03-17_04-26.xlsx'
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

null_number = 0
dict = {}
count_map = {"none": {}}
for i in range(10):
    dic_two = {}
    for j in range(i + 1, 10):
        dic_two[index_list[j]] = 0
    dict[index_list[i]] = dic_two
one_number = 0
two_number = 0
self_co = [0] * 10
line_number = 0
dic_method_2 = {}
labels = ['疫情中的众生相', '防控部署', '医疗物资保障与基础设施建设', '疫情中的经济', '疫情中的文化传播', '疫情中的民生', '新冠肺炎医治', '疫情中的国际社会', '新冠疫情动态', '疫情中的法制']

while line:
    category = []
    dic = json.loads(line)
    publish_time = dic["publish_time"]
    if "1999-01-19" < publish_time < "2050-02-20":
        line_number = line_number + 1
        print(line_number)
        topic = dic["topic_main"]
        topic_6 = dic["topic_6"]
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
        for i in range(10):
            for j in range(i + 1, 10):
                dict[index_list[i]][index_list[j]] += probability_list[i] * probability_list[j]
    line = file.readline()
for i in range(10):
    for j in range(i + 1, 10):
        dict[index_list[i]][index_list[j]] = dict[index_list[i]][index_list[j]] / line_number
print("dict")
print(dict)
for i in range(10):
    worksheet.write(i + 1, i + 1, 0)
    for j in range(i + 1, 10):
        worksheet.write(i + 1, j + 1, dict[index_list[i]][index_list[j]])
    for m in range(1, i + 1):
        worksheet.write(i + 1, m, dict[index_list[m - 1]][index_list[i]])
    worksheet.write(0, i + 1, labels[i])
    worksheet.write(i + 1, 0, labels[i])
workbook.close()

link_list = []
for i in range(10):
    for j in range(i + 1, 10):
        link = {"source": labels[i], "target": labels[j], "value": dict[index_list[i]][index_list[j]]}
        link_list.append(link)
pyperclip.copy(json.dumps(link_list, ensure_ascii=False))
data = []
for i in range(len(labels)):
    data_node = {"category": i, "name": labels[i], "x": 0, "y": 0}
    data.append(data_node)
