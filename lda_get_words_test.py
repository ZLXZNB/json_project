import tomotopy as tp
import xlsxwriter
import json

model_main = tp.LDAModel.load('D:/model/lda_final')
model_6 = tp.LDAModel.load('D:/test.lda.bin_new')
file_name = 'D:/eleven_topic.xlsx'
workbook = xlsxwriter.Workbook(file_name)
worksheet = workbook.add_worksheet('Sheet1')

main_words = []
six_words = []

words_main = []
words_6 = []

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
words = model_main.get_topic_words(1, top_n=10)
print(words)
print(dict(words))
a = dict(words)
print(a["病例"])
words2 = model_main.get_topic_words(2, top_n=10)
b = dict(words2)

c = [a, b]
print(c)
