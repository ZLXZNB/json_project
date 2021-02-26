import json
import threading
import time
from bert_serving.client import BertClient
import time
from threading import Thread
import _thread
# !/usr/bin/python3

import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        bert_thread()
        print("退出线程：" + self.name)


def get_str(word_list):
    str_words = ''
    for j in range(len(word_list)):
        if j < len(word_list) - 1:
            str_words = str_words + word_list[j] + ';'
        if j == len(word_list) - 1:
            str_words = str_words + word_list[j]
    return str_words


# file = open("D:/final_result.json", 'r', encoding='utf-8')
# line = file.readline()

def bert_thread():
    file = open("D:/find_query.json", 'r', encoding='utf-8')
    line = file.readline()
    text_list = []
    while line:
        dic = json.loads(line)
        content = dic["content"]
        text_list.append(content)
        line = file.readline()
    print("文本提取结束")
    print("bert开始")
    start = time.time()
    bc = BertClient("222.95.98.219", port=15555, port_out=15556)
    bc.encode(text_list)
    end = time.time()
    print("bert结束")
    print("时间为")
    print(end - start)


thread_list = []
for i in range(10):
    name = str(i+1)
    thread_list.append(myThread(i + 1, "Thread-"+name, i + 1))

# 开启新线程
for i in range(len(thread_list)):
    thread_list[i].start()
for i in range(len(thread_list)):
    thread_list[i].join()

print("退出主线程")
