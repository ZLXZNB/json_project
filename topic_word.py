import json
file = open("D:/final_result.json", 'r', encoding='utf-8')
line = file.readline()
content_all = []
number = 0
while line:
    number = number + 1
    dic = json.loads(line)
    print(number)
    line = file.readline()

