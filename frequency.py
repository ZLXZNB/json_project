import json

word_count = {}
count = 1
with open("D:/with_topics.txt", "r", encoding="utf-8") as input_file:
    line = input_file.readline()
    while line != '':
        print(count)
        record = json.loads(line)
        seg = record["seg"]
        for word in seg:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        line = input_file.readline()
        count += 1

# with open("D:/word_count.txt", "w", encoding="utf-8") as out_file:
#     out_file.write(json.dumps(word_count, ensure_ascii=False))