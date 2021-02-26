# a = "Bioengineered Bugs Call for Papers;"
# print(a.split(";;"))

import os

file_ch_dir = "D:/monetwaredata/ch"
file_en_dir = "D:/monetwaredata/en"
ms = open('D:/monetwaredata/ch.txt', 'a', encoding='utf-8')
files = os.listdir(file_ch_dir)
print(files)
files_dir = []
for file in files:
    files_dir.append(file_ch_dir + '/' + file)
    print(file_ch_dir + '/' + file)
# file_name = files_dir[0]
# file = open(file_name, 'r', encoding='utf-8')
# line = file.readline()
# while line:
#     line = file.readline()
number = 0
for file_dir in files_dir:
    file = open(file_dir, 'r', encoding='utf-8')
    line = file.readline()
    while line:
        number = number + 1
        print(number)
        print(line)
        if line == '\n':
            line = file.readline()
        else:
            if ':' in line:
                words = line.split(':')
                if words[0] != "Fund-基金" and words[0] != "Year-年":
                    ms.write(line)
                    line = file.readline()
                if words[0] == "Fund-基金":
                    ms.write(line.replace('\n', ''))
                    line = file.readline()
                if words[0] == "Year-年":
                    ms.write('\n')
                    ms.write(line)
                    line = file.readline()
            else:
                ms.write(line.replace('\n', ''))
                line = file.readline()
ms.close()

# for i in range(len(topic_6_bility)):
#     if topic_6_bility[i][0] > 0.5:
#         title_file_name = r"D:/topic_6/" + str(1) + ".txt"
#         ms = open(title_file_name, 'a', encoding='utf-8')
#         ms.write(topic_6_list[i])
#         ms.write('\n')
#         title_1.append(topic_6_list[i])
