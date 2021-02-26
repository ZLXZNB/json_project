length = []
for i in range(37):
    file_name = r"D:/topic_words/" + str(i) + ".txt"
    topic_file = open(file_name, 'r', encoding='utf-8')
    length.append(len(topic_file.readlines()))
print(length)

file = open("D:/final_result.json", 'r', encoding='utf-8')
line = file.readline()
number = 0
while line:
    line = file.readline()
    number = number + 1
print(number)
print(sum(length))