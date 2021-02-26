import os
#
# file_ch_dir = "D:/monetwaredata/ch"
# file_en_dir = "D:/monetwaredata/en"
ms = open('D:/monetwaredata/en_new.txt', 'a', encoding='utf-8')
# files = os.listdir(file_ch_dir)
# print(files)
# files_dir = []
# for file in files:
#     files_dir.append(file_ch_dir + '/' + file)
#     print(file_ch_dir + '/' + file)
file_name = "D:/monetwaredata/en.txt"
file = open(file_name, 'r', encoding='utf-8')
line = file.readline()
while line:
    if line == '\n':
        line = file.readline()
    else:
        ms.write(line)
        line = file.readline()
ms.close()
# number = 0
# for file_dir in files_dir:
#     file = open(file_dir, 'r', encoding='utf-8')
#     line = file.readline()
#     while line:
