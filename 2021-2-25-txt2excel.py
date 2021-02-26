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


file_result = 'D:/聚类人工调试.xlsx'
workbook = xlsxwriter.Workbook(file_result)
worksheet = workbook.add_worksheet('Sheet1')

# file = open("D:/final_result.json", 'r', encoding='utf-8')
# line = file.readline()
file = open("D:/聚类人工调试.txt", 'r', encoding='utf-8')
line = file.readline()
number = 0
while line:
    line_string = line.strip().replace('[', '').replace(']', '')
    worksheet.write(number, 0, line_string)
    number += 1
    line = file.readline()
workbook.close()
