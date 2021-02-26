# coding=utf-8
import json
import sys
import collections
import tomotopy as tp

from collections import Counter

file2 = open("D:/key_words.txt", 'r', encoding='utf-8')
keywords = []
for line in file2.readlines():
    keywords.append(line.strip().split('\t'))
print(keywords)
total_words = []
for word_list in keywords:
    total_words = total_words + word_list
total_words_remove = list(set(total_words))
print(total_words_remove)

file = open("D:/seg_result_custom.txt", 'r', encoding='utf-8')

seg = []
for line in file.readlines():
    dic = json.loads(line)
    # papers.append(dic)
    seg.append(dic["seg"])

# text = 0
# total_seg = []
# for total_list in seg:
#     total_seg = total_seg+total_list
#     text = text+1
#     print(text)

# print(total_seg)

# n=Counter(total_seg)
# frequency = []
# for i in total_words:
#     frequency.append(n[i])
# print(frequency)
frequency_of_word = {}
for word in total_words_remove:
    frequency_of_word[word] = 0
for line in seg:
    for word in line:
        if word in total_words_remove:
            frequency_of_word[word] = frequency_of_word[word] + 1

print(frequency_of_word)
