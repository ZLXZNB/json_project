import json

file = open("D:/final_result.json", 'r', encoding='utf-8')
line = file.readline()
number = 0
probability = []
counter = 0
topic_6_content = []
number_list = [0 for x in range(0, 14)]
while line:
    number = number + 1
    dic = json.loads(line)
    topic = dic["topic_main"]
    content = dic["seg"]
    print(number)
    if topic[5] > 0.25:
        topic_6_content.append(dic)
    line = file.readline()
for content in topic_6_content:
    for i in range(14):
        if content["topic_6"][i] > 0.25:
            number_list[i] = number_list[i] + 1

print(number_list)
print(sum(number_list))
# print(probability)
# quater = 0
# for content in probability:
#     if content > 0.25:
#         quater = quater+1
# print(quater/len(probability))
