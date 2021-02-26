import os

import pymongo

file_ch_dir = "D:/monetwaredata/ch"
file_en_dir = "D:/monetwaredata/en"
en_new_file = "D:/monetwaredata/en_new.txt"
files = os.listdir(file_ch_dir)
print(files)
files_dir = []
for file in files:
    files_dir.append(file_ch_dir + '/' + file)
    print(file_ch_dir + '/' + file)
file_name = files_dir[0]
file = open(file_name, 'r', encoding='utf-8')
line = file.readline()
while line:
    line = file.readline()


def get_valid_src_database_data(target_string):
    if ':' in target_string:
        words = target_string.split(':')
        if words[0] == "SrcDatabase-来源库":
            return words[1].strip()
        else:
            return ""
    else:
        return ""


def get_valid_title_data(target_string):
    if ':' in target_string:
        words = target_string.split(':')
        if words[0] == "Title-题名":
            return words[1].strip()
        else:
            return ""
    else:
        return ""


def get_valid_author_data(target_string):
    if ':' in target_string:
        words = target_string.split(':')
        if words[0] == "Author-作者":
            authors = []
            authors_all = words[1].strip().split(';')
            for author in authors_all:
                if author != '':
                    authors.append(author)
            return authors
        else:
            return []
    else:
        return []


def get_valid_organ_data(target_string):
    if ':' in target_string:
        words = target_string.split(':')
        if words[0] == "Organ-单位":
            organs = []
            organs_all = words[1].strip().split(';')
            for organ in organs_all:
                if organ != '':
                    organs.append(organ)
            return organs
        else:
            return []
    else:
        return []


def get_valid_source_data(target_string):
    if ':' in target_string:
        words = target_string.split(':')
        if words[0] == "Source-文献来源":
            return words[1].strip()
        else:
            return ""
    else:
        return ""


def get_valid_keyword_data(target_string):
    if ':' in target_string:
        words = target_string.split(':')
        if words[0] == "Keyword-关键词":
            keywords = []
            keywords_all = words[1].strip().split(';;')
            if len(keywords_all) == 1 and ";" in keywords_all[0]:
                keywords_en_all = keywords_all[0].strip().split(';')
                for keyword in keywords_en_all:
                    if keyword != '':
                        keywords.append(keyword)
                return keywords
            else:
                for key_word in keywords_all:
                    if key_word != '':
                        keywords.append(key_word)
                return keywords
        else:
            return []
    else:
        return []


def get_valid_summary_data(target_string):
    if ':' in target_string:
        words = target_string.split(':')
        if words[0] == "Summary-摘要":
            return words[1].strip()
        else:
            return ""
    else:
        return ""


def get_valid_pub_time_data(target_string):
    if ':' in target_string:
        words = target_string.split(':')
        if words[0] == "PubTime-发表时间":
            return words[1].strip()
        else:
            return ""
    else:
        return ""


def get_valid_FirstDuty_data(target_string):
    if ':' in target_string:
        words = target_string.split(':')
        if words[0] == "FirstDuty-第一责任人":
            organs = []
            organs_all = words[1].strip().split(';')
            for organ in organs_all:
                if organ != '':
                    organs.append(organ)
            return organs
        else:
            return []
    else:
        return []


def get_valid_year_data(target_string):
    if ':' in target_string:
        words = target_string.split(':')
        if words[0] == "Year-年":
            return words[1].strip()
        else:
            return ""
    else:
        return ""


def get_valid_period_data(target_string):
    if ':' in target_string:
        words = target_string.split(':')
        if words[0] == "Period-期":
            return words[1].strip()
        else:
            return ""
    else:
        return ""


def get_valid_pageCount_data(target_string):
    if ':' in target_string:
        words = target_string.split(':')
        if words[0] == "PageCount-页码":
            return words[1].strip()
        else:
            return ""
    else:
        return ""


def get_valid_CLC_data(target_string):
    if ':' in target_string:
        words = target_string.split(':')
        if words[0] == "CLC-中图分类号":
            return words[1].strip()
        else:
            return ""
    else:
        return ""


def get_valid_volume_data(target_string):
    if ':' in target_string:
        words = target_string.split(':')
        if words[0] == "Volume-卷":
            return words[1].strip()
        else:
            return ""
    else:
        return ""


def get_valid_Fund_data(target_string):
    if ':' in target_string:
        words = target_string.split(':')
        if words[0] == "Fund-基金":
            organs = []
            organs_all = words[1].strip().split(';;')
            for organ in organs_all:
                if organ != '':
                    organs.append(organ)
            return organs
        else:
            return []
    else:
        return []


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


file = open(en_new_file, 'r', encoding='utf-8')
lines = file.readlines()
position = []
# print(lines)
for i in range(len(lines)):
    if is_number(lines[i].split(':')[0]):
        position.append(i)
position.append(len(lines))

ch_biology = []
for i in range(len(position)-1):
    start = position[i]
    end = position[i + 1]
    ch_dictionary = {}
    for j in range(start + 1, end):
        # print(lines[j].split(':'))
        target = lines[j].split(':')[0]
        ch_dictionary["type"] = "english"
        if target == "SrcDatabase-来源库":
            ch_dictionary["SrcDataBase"] = get_valid_src_database_data(lines[j])
        if target == "Title-题名":
            ch_dictionary["title"] = get_valid_title_data(lines[j])
        if target == "Author-作者":
            ch_dictionary["author"] = get_valid_author_data(lines[j])
        if target == "Organ-单位":
            ch_dictionary["organ"] = get_valid_organ_data(lines[j])
        if target == "Source-文献来源":
            ch_dictionary["source"] = get_valid_source_data(lines[j])
        if target == "Keyword-关键词":
            ch_dictionary["keyword"] = get_valid_keyword_data(lines[j])
        if target == "Summary-摘要":
            ch_dictionary["summary"] = get_valid_summary_data(lines[j])
        if target == "PubTime-发表时间":
            ch_dictionary["PubTime"] = get_valid_pub_time_data(lines[j])
        if target == "FirstDuty-第一责任人":
            ch_dictionary["FirstDuty"] = get_valid_FirstDuty_data(lines[j])
        if target == "Fund-基金":
            ch_dictionary["Fund"] = get_valid_Fund_data(lines[j])
        if target == "Year-年":
            ch_dictionary["Year"] = get_valid_year_data(lines[j])
        if target == "Volume-卷":
            ch_dictionary["volume"] = get_valid_volume_data(lines[j])
        if target == "Period-期":
            ch_dictionary["period"] = get_valid_period_data(lines[j])
        if target == "PageCount-页码":
            ch_dictionary["pageCount"] = get_valid_pageCount_data(lines[j])
        if target == "CLC-中图分类号":
            ch_dictionary["CLC-中国分类号"] = get_valid_CLC_data(lines[j])
    ch_biology.append(ch_dictionary)
print(ch_biology)
client = pymongo.MongoClient("mongodb://192.168.1.142:27017/admin?connectTimeoutMS=10000&authSource=admin")
db = client["biology"]
collection = db["biology_data"]

collection.insert_many(ch_biology)
# while line:
#     if ':' in line:
#         target_value = line.split(':')
#         target = target_value[0]
#         if is_number(target):
#
#
#
#
#
#     line = file.readline()

#
# a = get_valid_keyword_data("Keyword-关键词: Diatoms;;Silicon;;Photoluminescence;;Biosensing")
# print(a)
