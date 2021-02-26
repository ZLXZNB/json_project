import pymongo
import requests
from bs4 import BeautifulSoup


def name_list(name_dict_list):
    name_list_result = []
    for name_dict in name_dict_list:
        name_list_result.append(name_dict["name"])
    return name_list_result


all_result = []
for i in range(173):
    if i == 0:
        target = "http://jinyici.xpcha.com" + "/" + "list_0.html"
    else:
        page = str(i + 1)
        target = "http://jinyici.xpcha.com" + "/" + "list_0_" + page + ".html"
    print(target)
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('dl', class_='shaixuan_5')
    for text in texts[0].find_all('a'):
        synonyms_list = []
        # print(text.get_text())
        content = text.get_text()
        # synonyms_list.append(content)
        # print(text.get('href'))
        href = text.get('href')
        url = "http://jinyici.xpcha.com" + "/" + href
        request = requests.get(url=url)
        html_text = request.text
        bf_text = BeautifulSoup(html_text)
        all_synonyms = bf_text.find_all('dl', class_="shaixuan_1")
        print(all_synonyms)
        for synonyms in all_synonyms[0].find_all('span'):
            synonyms_content = synonyms.get_text()
            synonyms_content = synonyms_content.replace("：", "")
            print(synonyms_content)
            synonyms_list.append(synonyms_content)
        synonyms_dictionary = {"name": content, "synonyms_list": synonyms_list}
        all_result.append(synonyms_dictionary)
# for element in all_result:
#     print(element)


one_phrase_name_list = name_list(all_result)

file = open("D:/word_library.txt", 'r', encoding='utf-8')
line = file.readline()
while line:
    split_line = line.split('=')
    if len(split_line) > 1:
        word_to_be_analyzed = split_line[1].split(' ')
        final_synonyms_list = []
        for word in word_to_be_analyzed:
            if word != "":
                final_synonyms_list.append(word)
        for final_word in final_synonyms_list:
            if final_word in one_phrase_name_list:
                for result in all_result:
                    if result["name"] == final_word:
                        for final_synonyms in final_synonyms_list:
                            if final_synonyms not in result["synonyms_list"]:
                                result["synonyms_list"].append(final_synonyms)
                                print("加入成功")
            else:
                all_result.append({"name": final_word, "synonyms_list": final_synonyms_list})
                print("加入成功")

    line = file.readline()

client = pymongo.MongoClient("mongodb://192.168.1.142:27017/admin?connectTimeoutMS=10000&authSource=admin")
db = client["ring_service"]
collection = db["rs_chinese_synonyms_dictionary"]

collection.insert_many(all_result)
