import json
import xlsxwriter
import codecs
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim import corpora, models

file_name = 'D:/topic_14.xlsx'
workbook = xlsxwriter.Workbook(file_name)
worksheet = workbook.add_worksheet('Sheet1')
# file = open("D:/final_result.json", 'r', encoding='utf-8')
# line = file.readline()
file = open("D:/final_result.json", 'r', encoding='utf-8')
line = file.readline()
content_all = []
number = 0
number_list = [0 for x in range(0, 14)]
while line:
    number = number + 1
    dic = json.loads(line)
    topic = dic["topic_6"]
    content = dic["seg"]
    print(number)
    for i in range(14):
        if topic[i] > 0.25:
            number_list[i] = number_list[i] + 1

    line = file.readline()
print(number_list)
print(sum(number_list))
for i in range(len(number_list)):
    title_name = 'A' + str(i + 1)
    worksheet.write(title_name, number_list[i])
workbook.close()