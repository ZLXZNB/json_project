import xlrd
import xlsxwriter
import os
import pymongo


def get_data(target_string):
    return target_string.strip().split(';')


file_ch_dir = "D:/monetwaredata/ch"
file_en_dir = "D:/monetwaredata/en"
en_new_file = "D:/monetwaredata/en_new.txt"

mysql_data_dir = "D:/monetwaredata/mysqldata"

files = os.listdir(mysql_data_dir)
files_dir = []
for file in files:
    files_dir.append(mysql_data_dir + '/' + file)
    print(mysql_data_dir + '/' + file)
# sh.cell(i, j).value
# file_name = files_dir[0]
# file = open(file_name, 'r', encoding='utf-8')
# line = file.readline()
# while line:
#     line = file.readline()
mysql_data_dictionary = []
for file_dir in files_dir:
    print(file_dir)
    wb = xlrd.open_workbook(file_dir)
    sh = wb.sheet_by_name('Sheet1')
    rows = sh.nrows
    for i in range(1, rows):
        mysql_dictionary = {"type": "english", "title": sh.cell(i, 1).value, "author": get_data(sh.cell(i, 2).value),
                            "author_introduce": sh.cell(i, 3).value, "summary": sh.cell(i, 4).value,
                            "highlight": sh.cell(i, 5).value, "keyword": get_data(sh.cell(i, 6).value),
                            "PubTime": sh.cell(i, 7).value, "volume": sh.cell(i, 8).value,
                            "period": sh.cell(i, 9).value, "url": sh.cell(i, 10).value, "pdf_url": sh.cell(i, 11).value,
                            "timestamp": sh.cell(i, 12).value}
        mysql_data_dictionary.append(mysql_dictionary)
client = pymongo.MongoClient("mongodb://192.168.1.142:27017/admin?connectTimeoutMS=10000&authSource=admin")
db = client["biology"]
collection = db["biology_data"]

collection.insert_many(mysql_data_dictionary)
