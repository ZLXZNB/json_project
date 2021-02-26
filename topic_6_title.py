import json
import re

file = open("D:/final_result.json", 'r', encoding='utf-8')
file_full = open("D:/dbnews.covid_wuhan_news.json", 'r', encoding='utf-8')
line = file.readline()
topic_6_list = []
topic_6_bility = []
title_1 = []
title_2 = []
title_3 = []
title_4 = []
title_5 = []
title_6 = []
title_7 = []
number = 0
while line:
    number = number + 1
    dic = json.loads(line)
    topic = dic["topic_main"]
    topic_6 = dic["topic_6"]
    content = dic["seg"]
    title = dic["title"]
    print(number)
    if topic[5] > 0.5:
        topic_6_list.append(title)
        topic_6_bility.append(topic_6)
    line = file.readline()

for i in range(len(topic_6_bility)):
    if topic_6_bility[i][0] > 0.5:
        title_file_name = r"D:/topic_6/" + str(1) + ".txt"
        ms = open(title_file_name, 'a', encoding='utf-8')
        ms.write(topic_6_list[i])
        ms.write('\n')
        title_1.append(topic_6_list[i])
    if topic_6_bility[i][10] > 0.5:
        title_file_name = r"D:/topic_6/" + str(2) + ".txt"
        ms = open(title_file_name, 'a', encoding='utf-8')
        ms.write(topic_6_list[i])
        ms.write('\n')
        title_2.append(topic_6_list[i])
    if topic_6_bility[i][1] > 0.5:
        title_file_name = r"D:/topic_6/" + str(3) + ".txt"
        ms = open(title_file_name, 'a', encoding='utf-8')
        ms.write(topic_6_list[i])
        ms.write('\n')
        title_3.append(topic_6_list[i])
    if topic_6_bility[i][2] > 0.5:
        title_file_name = r"D:/topic_6/" + str(4) + ".txt"
        ms = open(title_file_name, 'a', encoding='utf-8')
        ms.write(topic_6_list[i])
        ms.write('\n')
        title_4.append(topic_6_list[i])
    if topic_6_bility[i][8] > 0.5:
        title_file_name = r"D:/topic_6/" + str(4) + ".txt"
        ms = open(title_file_name, 'a', encoding='utf-8')
        ms.write(topic_6_list[i])
        ms.write('\n')
        title_4.append(topic_6_list[i])
    if topic_6_bility[i][7] > 0.5:
        title_file_name = r"D:/topic_6/" + str(5) + ".txt"
        ms = open(title_file_name, 'a', encoding='utf-8')
        ms.write(topic_6_list[i])
        ms.write('\n')
        title_5.append(topic_6_list[i])
    if topic_6_bility[i][6] > 0.5:
        title_file_name = r"D:/topic_6/" + str(6) + ".txt"
        ms = open(title_file_name, 'a', encoding='utf-8')
        ms.write(topic_6_list[i])
        ms.write('\n')
        title_6.append(topic_6_list[i])
    if topic_6_bility[i][5] > 0.5:
        title_file_name = r"D:/topic_6/" + str(7) + ".txt"
        ms = open(title_file_name, 'a', encoding='utf-8')
        ms.write(topic_6_list[i])
        ms.write('\n')
        title_7.append(topic_6_list[i])
    if topic_6_bility[i][12] > 0.5:
        title_file_name = r"D:/topic_6/" + str(7) + ".txt"
        ms = open(title_file_name, 'a', encoding='utf-8')
        ms.write(topic_6_list[i])
        ms.write('\n')
        title_7.append(topic_6_list[i])
line_full = file_full.readline()
number = 0
while line_full:
    number = number + 1
    dic = json.loads(line_full)
    title = dic["tt"]
    content = dic["ct"]
    print(number)
    if title in title_1:
        path_name = r"D:/topic_6/" + str(1) + "/"
        text_name = re.sub(r'[?\\|<>/*:\\…"]', '', dic["tt"])
        text_name = text_name.replace('\t', '')
        text_name = text_name.replace('\n', '')
        file_name = path_name + text_name + ".txt"
        ms = open(file_name, 'w', encoding='utf-8')
        data = dic["ct"]
        if data is not None:
            ms.write(data)
            print("写入完成")
    if title in title_2:
        path_name = r"D:/topic_6/" + str(2) + "/"
        text_name = re.sub(r'[?\\|<>/*:\\…"]', '', dic["tt"])
        text_name = text_name.replace('\t', '')
        text_name = text_name.replace('\n', '')
        file_name = path_name + text_name + ".txt"
        ms = open(file_name, 'w', encoding='utf-8')
        data = dic["ct"]
        if data is not None:
            ms.write(data)
            print("写入完成")
    if title in title_3:
        path_name = r"D:/topic_6/" + str(3) + "/"
        text_name = re.sub(r'[?\\|<>/*:\\…"]', '', dic["tt"])
        text_name = text_name.replace('\t', '')
        text_name = text_name.replace('\n', '')
        file_name = path_name + text_name + ".txt"
        ms = open(file_name, 'w', encoding='utf-8')
        data = dic["ct"]
        if data is not None:
            ms.write(data)
            print("写入完成")
    if title in title_4:
        path_name = r"D:/topic_6/" + str(4) + "/"
        text_name = re.sub(r'[?\\|<>/*:\\…"]', '', dic["tt"])
        text_name = text_name.replace('\t', '')
        text_name = text_name.replace('\n', '')
        file_name = path_name + text_name + ".txt"
        ms = open(file_name, 'w', encoding='utf-8')
        data = dic["ct"]
        if data is not None:
            ms.write(data)
            print("写入完成")
    if title in title_5:
        path_name = r"D:/topic_6/" + str(5) + "/"
        text_name = re.sub(r'[?\\|<>/*:\\…"]', '', dic["tt"])
        text_name = text_name.replace('\t', '')
        text_name = text_name.replace('\n', '')
        file_name = path_name + text_name + ".txt"
        ms = open(file_name, 'w', encoding='utf-8')
        data = dic["ct"]
        if data is not None:
            ms.write(data)
            print("写入完成")
    if title in title_6:
        path_name = r"D:/topic_6/" + str(6) + "/"
        text_name = re.sub('[\?\\|<>/\*:…\\\\\\\n\\\t"]', '', dic["tt"])
        text_name = text_name.replace('\t', '')
        text_name = text_name.replace('\n', '')
        file_name = path_name + text_name + ".txt"
        ms = open(file_name, 'w', encoding='utf-8')
        data = dic["ct"]
        if data is not None:
            ms.write(data)
            print("写入完成")
    if title in title_7:
        path_name = r"D:/topic_6/" + str(7) + "/"
        text_name = re.sub(r'[?\\|<>/*:\\…"]', '', dic["tt"])
        text_name = text_name.replace('\t', '')
        text_name = text_name.replace('\n', '')
        file_name = path_name + text_name + ".txt"
        ms = open(file_name, 'w', encoding='utf-8')
        data = dic["ct"]
        if data is not None:
            ms.write(data)
            print("写入完成")
    line_full = file_full.readline()

