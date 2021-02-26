import json
import xlsxwriter
import mysql.connector.pooling
import pymongo


def sort_dict_by_value(d, reverse=True):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))


client = pymongo.MongoClient("mongodb://192.168.1.142:27017/admin?connectTimeoutMS=10000&authSource=admin")
db = client["biology"]
collection = db["biology_data"]

organ_article_file = "D:/monetwaredata/organ-article_count.xlsx"
workbook = xlsxwriter.Workbook(organ_article_file)
worksheet = workbook.add_worksheet('Sheet1')

organ_dictionary = {}
first_author_dictionary = {}
for x in collection.find():
    if "organ" in x.keys():
        organs = x["organ"]
        for organ in organs:
            if organ is not None and organ != "":
                if organ in organ_dictionary:
                    if organs[0] == organ:
                        organ_dictionary[organ] += 1
                    else:
                        organ_dictionary[organ] += 0.5
                else:
                    if organs[0] == organ:
                        organ_dictionary[organ] = 1
                    else:
                        organ_dictionary[organ] = 0.5
    if "author" in x.keys():
        authors = x["author"]
        if authors:
            if authors[0] is not None and authors[0] != "":
                if authors[0] in first_author_dictionary:
                    first_author_dictionary[authors[0]] += 1
                else:
                    first_author_dictionary[authors[0]] = 1
final_result = sort_dict_by_value(organ_dictionary)
keys_list = list(final_result.keys())
for i in range(len(keys_list)):
    print(i)
    worksheet.write(i + 1, 0, keys_list[i])
    worksheet.write(i + 1, 1, final_result[keys_list[i]])
workbook.close()
first_author_count = 0
for key in list(first_author_dictionary.keys()):
    first_author_count += first_author_dictionary[key]
print("第一作者数量为")
print(first_author_count)
