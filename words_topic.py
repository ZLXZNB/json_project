import tomotopy as tp
import xlsxwriter
import json
from collections import Counter

model_main = tp.LDAModel.load('D:/model/lda_final')
model_6 = tp.LDAModel.load('D:/test.lda.bin_new')
file_name = 'D:/eleven_topic.xlsx'
workbook = xlsxwriter.Workbook(file_name)
worksheet = workbook.add_worksheet('Sheet1')

main_words = []
six_words = []

words_main = []
words_6 = []
words_main_json = []
words_6_json = []
one_topic = []
two_topic = []
three_topic = []
four_topic = []
five_topic = []
six_topic = []
seven_topic = []
eight_topic = []
nine_topic = []
ten_topic = []
eleven_topic = []

for i in range(37):
    words = model_main.get_topic_words(i, top_n=500)
    words_main_json.append(dict(words))
    topic_words = []
    for element in words:
        topic_words.append(element[0])
    words_main.append(topic_words)

    str_word = ''
    for j in range(len(topic_words)):
        if j < len(topic_words) - 1:
            str_word = str_word + topic_words[j] + ';'
        if j == len(topic_words):
            str_word = str_word + topic_words[j]
    main_words.append(str_word)

for i in range(14):
    words = model_6.get_topic_words(i, top_n=100)
    words_6_json.append(dict(words))
    topic_words = []
    for element in words:
        topic_words.append(element[0])
    words_6.append(topic_words)
    str_word = ''
    for j in range(len(topic_words)):
        if j < len(topic_words) - 1:
            str_word = str_word + topic_words[j] + ';'
        if j == len(topic_words):
            str_word = str_word + topic_words[j]
    # worksheet.write(title_name, str_word)
    six_words.append(str_word)
one_topic = words_main[26]
two_topic = words_main[1] + words_main[14] + words_main[33]
three_topic = words_main[12] + words_main[20] + words_main[28]
four_topic = words_main[11] + words_main[17]
five_topic = words_main[4] + words_main[6] + words_main[22] + words_main[27] + words_main[31] + words_main[32]
six_topic = words_main[8] + words_main[18] + words_main[24] + words_main[25] + words_main[35]
seven_topic = words_main[0] + words_main[3] + words_main[15] + words_main[16] + words_main[29]
eight_topic = words_main[2] + words_main[9] + words_main[10] + words_main[13] + words_main[34] + words_main[36]
nine_topic = words_main[7] + words_main[19] + words_main[21]
ten_topic = words_6[0] + words_6[1] + words_6[2] + words_6[5] + words_6[6] + words_6[7] + words_6[8] + words_6[10] + \
            words_6[11] + words_6[
                12] + words_6[13]
eleven_topic = words_main[23] + words_main[30]

one_dict = words_main_json[26]
two_dict = dict(Counter(words_main_json[1]) + Counter(words_main_json[14]) + Counter(words_main_json[33]))
three_dict = dict(Counter(words_main_json[12]) + Counter(words_main_json[20]) + Counter(words_main_json[28]))
four_dict = dict(Counter(words_main_json[11]) + Counter(words_main_json[17]))
five_dict = dict(Counter(words_main_json[4]) + Counter(words_main_json[6]) + Counter(words_main_json[22]) + Counter(
    words_main_json[27]) + Counter(words_main_json[31]) + Counter(words_main_json[32]))
six_dict = dict(Counter(words_main_json[8]) + Counter(words_main_json[18]) + Counter(words_main_json[24]) + Counter(
    words_main_json[25]) + Counter(words_main_json[35]))
seven_dict = dict(Counter(words_main_json[0]) + Counter(words_main_json[3]) + Counter(words_main_json[15]) + Counter(
    words_main_json[16]) + Counter(words_main_json[29]))
eight_dict = dict(Counter(words_main_json[2]) + Counter(words_main_json[9]) + Counter(words_main_json[10]) + Counter(
    words_main_json[13]) + Counter(words_main_json[34]) + Counter(words_main_json[36]))
nine_dict = dict(Counter(words_main_json[7]) + Counter(words_main_json[19]) + Counter(words_main_json[21]))
ten_dict = dict(
    Counter(words_6_json[0]) + Counter(words_6_json[1]) + Counter(words_6_json[2]) + Counter(words_6_json[5]) + Counter(
        words_6_json[6]) + Counter(words_6_json[7]) + Counter(words_6_json[8]) + Counter(words_6_json[10]) + Counter(
        words_6_json[11]) + Counter(words_6_json[12]) + Counter(words_6_json[13]))
eleven_dict = dict(Counter(words_main_json[23]) + Counter(words_main_json[30]))


# word_count = {}
# count = 1
# with open("D:/final_result.json", "r", encoding="utf-8") as input_file:
#     line = input_file.readline()
#     while line != '':
#         print(count)
#         record = json.loads(line)
#         seg = record["seg"]
#         for word in seg:
#             if word in word_count:
#                 word_count[word] += 1
#             else:
#                 word_count[word] = 1
#         line = input_file.readline()
#         count += 1


def extraction(a, b):
    count = []
    for word in a:
        count.append(b[word])
    word_count_new = {}
    for i in range(len(a)):
        word_count_new[a[i]] = count[i]
    d_order = sorted(word_count_new.items(), key=lambda x: x[1], reverse=True)
    words_list = []
    for index in range(100):
        words_list.append(d_order[index][0])
    return words_list


one_list = extraction(one_topic, one_dict)
two_list = extraction(two_topic, two_dict)
three_list = extraction(three_topic, three_dict)
four_list = extraction(four_topic, four_dict)
five_list = extraction(five_topic, five_dict)
six_list = extraction(six_topic, six_dict)
seven_list = extraction(seven_topic, seven_dict)
eight_list = extraction(eight_topic, eight_dict)
nine_list = extraction(nine_topic, nine_dict)
ten_list = extraction(ten_topic, ten_dict)
eleven_list = extraction(eleven_topic, eleven_dict)


def get_str(word_list):
    str_words = ''
    for j in range(len(word_list)):
        if j < len(word_list) - 1:
            str_words = str_words + word_list[j] + ';'
        if j == len(word_list) - 1:
            str_words = str_words + word_list[j]
    return str_words


worksheet.write(0, 0, get_str(one_list))
worksheet.write(1, 0, get_str(two_list))
worksheet.write(2, 0, get_str(three_list))
worksheet.write(3, 0, get_str(four_list))
worksheet.write(4, 0, get_str(five_list))
worksheet.write(5, 0, get_str(six_list))
worksheet.write(6, 0, get_str(seven_list))
worksheet.write(7, 0, get_str(eight_list))
worksheet.write(8, 0, get_str(nine_list))
worksheet.write(9, 0, get_str(ten_list))
worksheet.write(10, 0, get_str(eleven_list))

workbook.close()
