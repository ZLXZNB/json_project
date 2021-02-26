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


file_name = 'D:/topic_co.xlsx'
workbook = xlsxwriter.Workbook(file_name)
worksheet = workbook.add_worksheet('Sheet1')

file_co = 'D:/new_co/co_matrix.xlsx'
workbook_2 = xlsxwriter.Workbook(file_co)
worksheet_2 = workbook_2.add_worksheet('Sheet1')

list_only = [0] * 11

# file = open("D:/final_result.json", 'r', encoding='utf-8')
# line = file.readline()
file = open("D:/final_result.json", 'r', encoding='utf-8')
line = file.readline()
content_all = []
number = 0
number_list = [0 for x in range(0, 14)]
index_list = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一']
null_number = 0
dict = {}
count_map = {"none": {}}
for i in range(11):
    dic_two = {}
    for j in range(i + 1, 11):
        dic_two[index_list[j]] = 0
    dict[index_list[i]] = dic_two
print(dict)
one_number = 0
two_number = 0
while line:
    category = []
    dic = json.loads(line)
    topic = dic["topic_main"]
    topic_6 = dic["topic_6"]
    content = dic["seg"]
    print(number)
    if topic[26] > 0.25:
        category.append('一')
    if topic[1] > 0.25 or topic[14] > 0.25 or topic[33] > 0.25:
        category.append('二')
    if topic[12] > 0.25 or topic[20] > 0.25 or topic[28] > 0.25:
        category.append('三')
    if topic[11] > 0.25 or topic[17] > 0.25:
        category.append('四')
    if topic[4] > 0.25 or topic[6] > 0.25 or topic[27] > 0.25 or topic[22] > 0.25 or topic[31] > 0.25 or topic[
        32] > 0.25:
        category.append('五')
    if topic[24] > 0.25 or topic[35] > 0.25 or topic[18] > 0.25 or topic[25] > 0.25 or topic[8] > 0.25:
        category.append('六')
    if topic[0] > 0.25 or topic[15] > 0.25 or topic[16] > 0.25 or topic[3] > 0.25 or topic[29] > 0.25:
        category.append('七')
    if topic[9] > 0.25 or topic[13] > 0.25 or topic[36] > 0.25 or topic[10] > 0.25 or topic[2] > 0.25 or topic[
        34] > 0.25:
        category.append('八')
    if topic[19] > 0.25 or topic[21] > 0.25 or topic[7] > 0.25:
        category.append('九')
    if topic[5] > 0.25:
        category.append('十')
    if topic[23] > 0.25 or topic[30] > 0.25:
        category.append('十一')

    for i in range(11):
        for j in range(i + 1, 11):
            if index_list[i] in category and index_list[j] in category:
                print('匹配成功')
                dict[index_list[i]][index_list[j]] += 1

    for i in range(11):
        if category == [index_list[i]]:
            list_only[i] = list_only[i] + 1

    if len(category) == 1:
        topic = category[0]
        if topic not in count_map["none"]:
            count_map["none"][topic] = 1
        else:
            count_map["none"][topic] += 1

    for topic in category:
        if topic not in count_map:
            count_map[topic] = {}

        for another in category:
            if another in count_map[topic]:
                count_map[topic][another] += 1
            else:
                count_map[topic][another] = 1

    if category:
        number = number + 1
        worksheet.write(number - 1, 0, get_str(category))
    line = file.readline()
workbook.close()
print(count_map)
print(dict)
for i in range(11):
    worksheet_2.write(i + 1, i + 1, 0)
    for j in range(i + 1, 11):
        worksheet_2.write(i + 1, j + 1, dict[index_list[i]][index_list[j]])
    for m in range(1, i + 1):
        worksheet_2.write(i + 1, m, dict[index_list[m - 1]][index_list[i]])
for i in range(11):
    worksheet_2.write(i + 1, 12, list_only[i])
    worksheet_2.write(i + 1, 0, index_list[i])
    worksheet_2.write(0, i + 1, index_list[i])
workbook_2.close()
