import time

from ddparser import DDParser
from LAC import LAC
import xlsxwriter
import json
import re

from text_seg.tokenizer import ansj_tokenize

sentence_pattern_dictionary = {1: "主谓宾", 2: "主谓", 3: "对字句", 4: "把字句", 5: "被字句", 6: "子句结构"}

final_svo_result = []
lac = LAC(mode='lac')
ddp = DDParser()


def string_to_list(a):
    if a.split(','):
        return a.split(',')
    else:
        return [a]


def split_sentences(content):
    return [sentence for sentence in re.split(r'[？?！“”""!。；;：:\n\r]', content) if sentence]


def get_sub_relationship(syntax_dictionary):
    relationship_list = []
    children_list = syntax_dictionary["children"]
    for dictionary in children_list:
        name_list = string_to_list(dictionary["name"])
        relationship = name_list[1]
        relationship_list.append(relationship)
    return relationship_list


def get_decoration(decoration_node_list):
    decoration_list = []
    for decoration_node in decoration_node_list:
        if "children" not in decoration_node.keys():
            if string_to_list(decoration_node["name"])[1] != "MT":
                decoration_list.append(string_to_list(decoration_node["name"])[0])
        else:
            decoration_string = string_to_list(decoration_node["name"])[0]
            final_string = ""
            children_node_list = get_decoration(decoration_node["children"])
            # print("children_node_list")
            # print(children_node_list)
            final_list = []
            if children_node_list:
                for i in range(len(children_node_list)):
                    if i < len(children_node_list) - 1:
                        final_list.append(children_node_list[i] + decoration_string)
                        final_string = final_string + children_node_list[i] + decoration_string + ","
                    else:
                        final_string = final_string + children_node_list[i] + decoration_string
                        final_list.append(children_node_list[i] + decoration_string)
            else:
                final_list.append(decoration_string)

            for text_value in final_list:
                decoration_list.append(text_value)
            # decoration_list.append(final_string)
    return decoration_list


def judgment_sentence_pattern(result_dictionary):
    sentence_pattern = 1
    relationship_list = []
    children_list = result_dictionary["children"]
    for dictionary in children_list:
        name_list = string_to_list(dictionary["name"])
        relationship = name_list[1]
        if relationship == "IC":
            sentence_pattern = 6
            return sentence_pattern

    for dictionary in children_list:
        name_list = string_to_list(dictionary["name"])
        name = name_list[0]
        relationship = name_list[1]
        relationship_list.append(relationship)

        if name == "对" and relationship == "ADV":
            sentence_pattern = 3
            return sentence_pattern
        else:
            if relationship == "POB":
                if name == "把":
                    sentence_pattern = 4
                    return sentence_pattern
                if name == "被":
                    sentence_pattern = 5
                    return sentence_pattern

    if "VOB" in relationship_list and "IC" not in relationship_list:
        sentence_pattern = 1
    if "VOB" not in relationship_list and "IC" not in relationship_list:
        sentence_pattern = 2

    return sentence_pattern


def sentence_analysis(syntax_dictionary):
    sentence_type = judgment_sentence_pattern(syntax_dictionary)

    # print("句式种类")
    # print(sentence_type)
    # 根据句式选择不同的方法
    if sentence_type == 1:
        # print(subject_verb_object(syntax_dictionary))
        return subject_verb_object(syntax_dictionary)
    if sentence_type == 2:
        # print(subject_verb(syntax_dictionary))
        return subject_verb(syntax_dictionary)
    if sentence_type == 3:
        # print(dui_sentence(syntax_dictionary))
        return dui_sentence(syntax_dictionary)
    if sentence_type == 4:
        # print(ba_sentence(syntax_dictionary))
        return ba_sentence(syntax_dictionary)
    if sentence_type == 5:
        # print(bei_sentence(syntax_dictionary))
        return bei_sentence(syntax_dictionary)
    if sentence_type == 6:
        # print(sub_sentence(syntax_dictionary))
        return sub_sentence(syntax_dictionary)


def subject_verb_object(result_dictionary):
    subject = ""
    object = ""
    subject_decorate = []
    verb_decorate = []
    vv_object = []
    vv_decoration = []
    object_decorate = []
    verb = string_to_list(result_dictionary["name"])[0]
    children_list = result_dictionary["children"]
    for dictionary in children_list:
        name_list = string_to_list(dictionary["name"])
        name = name_list[0]
        relationship = name_list[1]
        if relationship == "VV":
            if "children" in dictionary.keys():
                vv_list = dictionary["children"]
            else:
                vv_list = []

            verb = verb + ";" + name
            for vv_dictionary in vv_list:
                if string_to_list(vv_dictionary["name"])[1] == "CMP":
                    vv_decoration.append(string_to_list(vv_dictionary["name"])[0])
                    if "children" in vv_dictionary.keys():
                        vv_list = vv_dictionary["children"]
                    else:
                        vv_list = []

            vv_object = get_decoration(vv_list)
        if relationship == "ADV" and name != "对":
            verb_decorate.append(name)
            if "children" in dictionary.keys():
                for element in get_decoration(dictionary["children"]):
                    verb_decorate.append(element)

        if relationship == "CMP":
            verb_decorate.append(name)
            if "children" in dictionary.keys():
                for element in get_decoration(dictionary["children"]):
                    verb_decorate.append(element)

        if relationship == "SBV":
            subject = name
            if "children" in dictionary.keys():
                subject_decorate = get_decoration(dictionary["children"])

        if relationship == "VOB":
            object = name
            if "children" in dictionary.keys():
                categorization_list = []
                for children_dict in dictionary["children"]:
                    categorization_list.append(string_to_list(children_dict["name"])[1])
                if "SBV" in categorization_list and "VOB" in categorization_list:
                    true_dictionary = dictionary
                    # sentence_analysis(true_dictionary)
                    sentence_type = judgment_sentence_pattern(true_dictionary)
                    # print("句式种类")
                    # print(sentence_type)
                    # 根据句式选择不同的方法
                    if sentence_type == 1:
                        subject_verb_object(true_dictionary)
                    if sentence_type == 2:
                        subject_verb(true_dictionary)
                    if sentence_type == 3:
                        dui_sentence(true_dictionary)
                    if sentence_type == 4:
                        ba_sentence(true_dictionary)
                    if sentence_type == 5:
                        bei_sentence(true_dictionary)
                    if sentence_type == 6:
                        sub_sentence(true_dictionary)
                else:
                    object_decorate = get_decoration(dictionary["children"])
    if vv_decoration:
        for element in vv_decoration:
            verb_decorate.append(element)

    if not vv_object:
        dict_final = {"实施者": {"name": subject, "decoration": subject_decorate},
                      "动作": {"name": verb, "decoration": verb_decorate},
                      "承受者": {"name": object, "decoration": object_decorate}}
    else:
        for vv_object_element in vv_object:
            object = object + ";" + vv_object_element
        dict_final = {"实施者": {"name": subject, "decoration": subject_decorate},
                      "动作": {"name": verb, "decoration": verb_decorate},
                      "承受者": {"name": object, "decoration": object_decorate}}

    final_svo_result.append(dict_final)
    return dict_final


def subject_verb(result_dictionary):
    subject = ""
    subject_decorate = []
    verb_decorate = []
    verb = string_to_list(result_dictionary["name"])[0]
    children_list = result_dictionary["children"]
    for dictionary in children_list:
        name_list = string_to_list(dictionary["name"])
        name = name_list[0]
        relationship = name_list[1]
        if relationship == "ADV" and name != "对":
            verb_decorate.append(name)
            if "children" in dictionary.keys():
                for element in get_decoration(dictionary["children"]):
                    verb_decorate.append(element)

        if relationship == "CMP":
            verb_decorate.append(name)
            if "children" in dictionary.keys():
                for element in get_decoration(dictionary["children"]):
                    verb_decorate.append(element)

        if relationship == "SBV":
            subject = name
            if "children" in dictionary.keys():
                subject_decorate = get_decoration(dictionary["children"])
        #
        # if relationship == "VOB":
        #     object = name
        #     if "children" in dictionary.keys():
        #         object_decorate = get_decoration(dictionary["children"])

    dict_final = {"实施者": {"name": subject, "decoration": subject_decorate},
                  "动作": {"name": verb, "decoration": verb_decorate}}
    final_svo_result.append(dict_final)
    return dict_final


def dui_sentence(result_dictionary):
    subject = ""
    object = ""
    subject_decorate = []
    verb_decorate = []
    object_decorate = []
    verb = string_to_list(result_dictionary["name"])[0]
    children_list = result_dictionary["children"]
    for dictionary in children_list:
        name_list = string_to_list(dictionary["name"])
        name = name_list[0]
        relationship = name_list[1]
        if relationship == "ADV" and name != "对":
            verb_decorate.append(name)
        if relationship == "CMP":
            verb_decorate.append(name)
        if relationship == "ADV" and name == "对":
            if "children" in dictionary.keys():
                for relation_dict in dictionary["children"]:
                    if string_to_list(relation_dict["name"])[1] == "POB":
                        object = string_to_list(relation_dict["name"])[0]
                        if "children" in relation_dict.keys():
                            solid_dictionary = []
                            for value in relation_dict["children"]:
                                if string_to_list(value["name"])[1] == "COO":
                                    object = object + "," + string_to_list(value["name"])[0]
                                else:
                                    if string_to_list(value["name"])[1] != "MT":
                                        solid_dictionary.append(value)
                            object_decorate = get_decoration(solid_dictionary)

        if relationship == "SBV":
            subject = name
            if "children" in dictionary.keys():
                subject_decorate = get_decoration(dictionary["children"])
        if relationship == "VOB":
            verb = verb + name
            if "children" in dictionary.keys():
                verb_decorate = get_decoration(dictionary["children"])
        #
        # if relationship == "VOB":
        #     object = name
        #     if "children" in dictionary.keys():
        #         object_decorate = get_decoration(dictionary["children"])

    dict_final = {"实施者": {"name": subject, "decoration": subject_decorate},
                  "动作": {"name": verb, "decoration": verb_decorate},
                  "承受者": {"name": object, "decoration": object_decorate}}
    final_svo_result.append(dict_final)
    return dict_final


def ba_sentence(result_dictionary):
    subject = ""
    object = ""
    subject_decorate = []
    verb_decorate = []
    object_decorate = []
    verb = string_to_list(result_dictionary["name"])[0]
    children_list = result_dictionary["children"]
    for dictionary in children_list:
        name_list = string_to_list(dictionary["name"])
        name = name_list[0]
        relationship = name_list[1]
        if relationship == "ADV" and name != "对":
            verb_decorate.append(name)
        if relationship == "CMP":
            verb_decorate.append(name)

        if relationship == "SBV":
            subject = name
            if "children" in dictionary.keys():
                subject_decorate = get_decoration(dictionary["children"])

        if relationship == "POB" and name == "把":
            if "children" in dictionary.keys():
                for relation_dict in dictionary["children"]:
                    if string_to_list(relation_dict["name"])[1] == "POB":
                        object = string_to_list(relation_dict["name"])[0]
                        if "children" in relation_dict.keys():
                            solid_dictionary = []
                            for value in relation_dict["children"]:
                                if string_to_list(value["name"])[1] == "COO":
                                    object = object + "," + string_to_list(value["name"])[0]
                                else:
                                    if string_to_list(value["name"])[1] != "MT":
                                        solid_dictionary.append(value)
                            object_decorate = get_decoration(solid_dictionary)

        #
        # if relationship == "VOB":
        #     object = name
        #     if "children" in dictionary.keys():
        #         object_decorate = get_decoration(dictionary["children"])

    dict_final = {"实施者": {"name": subject, "decoration": subject_decorate},
                  "动作": {"name": verb, "decoration": verb_decorate},
                  "承受者": {"name": object, "decoration": object_decorate}}
    final_svo_result.append(dict_final)
    return dict_final


def bei_sentence(result_dictionary):
    subject = ""
    object = ""
    subject_decorate = []
    verb_decorate = []
    object_decorate = []
    verb = string_to_list(result_dictionary["name"])[0]
    children_list = result_dictionary["children"]
    for dictionary in children_list:
        name_list = string_to_list(dictionary["name"])
        name = name_list[0]
        relationship = name_list[1]
        if relationship == "ADV" and name != "对":
            verb_decorate.append(name)
        if relationship == "CMP":
            verb_decorate.append(name)

        if relationship == "SBV":
            object = name
            if "children" in dictionary.keys():
                object_decorate = get_decoration(dictionary["children"])
        if relationship == "POB" and name == "被":
            if "children" in dictionary.keys():
                for relation_dict in dictionary["children"]:
                    if string_to_list(relation_dict["name"])[1] == "POB":
                        subject = string_to_list(relation_dict["name"])[0]
                        if "children" in relation_dict.keys():
                            solid_dictionary = []
                            for value in relation_dict["children"]:
                                if string_to_list(value["name"])[1] == "COO":
                                    subject = subject + "," + string_to_list(value["name"])[0]
                                else:
                                    if string_to_list(value["name"])[1] != "MT":
                                        solid_dictionary.append(value)
                            subject_decorate = get_decoration(solid_dictionary)

    dict_final = {"实施者": {"name": subject, "decoration": subject_decorate},
                  "动作": {"name": verb, "decoration": verb_decorate},
                  "承受者": {"name": object, "decoration": object_decorate}}
    final_svo_result.append(dict_final)
    return dict_final


def sub_sentence(result_dictionary):
    IC_list = []
    result_list = []
    subject = ""
    object = ""
    subject_decorate = []
    verb_decorate = []
    object_decorate = []
    relationship_list = get_sub_relationship(result_dictionary)
    verb = string_to_list(result_dictionary["name"])[0]
    children_list = result_dictionary["children"]
    if "IC" in relationship_list and "SBV" in relationship_list:
        # print("有主语")
        sbv_name = ""
        for dictionary in children_list:
            if string_to_list(dictionary["name"])[1] == "SBV":
                sbv_name = dictionary["name"]
        children_new = []
        for dictionary in children_list:
            name_list = string_to_list(dictionary["name"])
            name = name_list[0]
            relationship = name_list[1]
            if relationship != "IC":
                children_new.append(dictionary)
            if relationship == "IC":
                if "children" in dictionary.keys():
                    sub_children = dictionary["children"]
                else:
                    sub_children = []
                ic_sub_relationship = get_sub_relationship(dictionary)
                if "SBV" not in ic_sub_relationship:
                    sub_children.append({"name": sbv_name, "value": 10000})
                new_dictionary = {"name": name + "," + "HED", "children": sub_children}
                IC_list.append(new_dictionary)
        new_main_dictionary = {"name": verb + "," + "HED", "children": children_new}
        for ic_sentence in IC_list:
            sentence_analysis(ic_sentence)
        return sentence_analysis(new_main_dictionary)

    if "IC" in relationship_list and "SBV" not in relationship_list:
        # print("无主语")
        children_new = []
        for dictionary in children_list:
            name_list = string_to_list(dictionary["name"])
            name = name_list[0]
            relationship = name_list[1]
            if relationship != "IC":
                children_new.append(dictionary)
            if relationship == "IC":
                if "children" not in dictionary.keys():
                    new_dictionary = {"name": name + "," + "HED", "children": []}
                else:
                    sub_children = dictionary["children"]
                    new_dictionary = {"name": name + "," + "HED", "children": sub_children}
                if sentence_analysis(new_dictionary) is not None:
                    needed_sbv = sentence_analysis(new_dictionary)["实施者"]["name"]
                else:
                    needed_sbv = new_dictionary["name"]
                if sentence_analysis(new_dictionary) is not None:
                    sbv_decoration = sentence_analysis(new_dictionary)["实施者"]["decoration"]
                else:
                    sbv_decoration = []
                sbv_children = []
                if sbv_decoration:
                    for decoration in sbv_decoration:
                        sbv_children.append({"name": decoration + "," + "ATT", "value": 10000})
                    children_new.append({"name": needed_sbv + "," + "SBV", "children": sbv_children})
                else:
                    children_new.append({"name": needed_sbv + "," + "SBV", "value": 10000})
        sbv_added_dictionary = {"name": verb + "," + "HED", "children": children_new}
        return sentence_analysis(sbv_added_dictionary)
    #
    # dict_final = {"实施者": {"name": subject, "decoration": subject_decorate},
    #               "动作": {"name": verb, "decoration": verb_decorate},
    #               "承受者": {"name": object, "decoration": object_decorate}}
    # return dict_final


def event_extraction(sentence):
    final_svo_result.clear()
    # sentence = sentence
    # seg_list = [["吉林省", "通报", "一名", "新冠肺炎", "无症状", "患者", "曾", "在", "不同地点", "进行", "培训", "授课"]]
    # lac_result = lac.run(sentence)
    analysis_result = ddp.parse_seg(sentence)
    # print(analysis_result)
    # ner_result = lac_result[1]
    # number = 0
    # per_number = []
    # for entity in ner_result:
    #     if entity == 'PER':
    #         per_number.append(number)
    #         number = number + 1
    #     if entity != 'PER':
    #         number = number + 1
    # print(analysis_result)
    words = analysis_result[0]["word"]
    head = analysis_result[0]["head"]
    sentence_tree = analysis_result[0]["deprel"]
    tree_structure = []
    # print(words)
    # print(head)

    depth_list = []
    for node_index in head:
        if node_index == 0:
            depth_list.append(1)
            continue
        depth = 1
        while head[node_index - 1] != 0:
            depth = depth + 1
            node_index = head[node_index - 1]
        if head[node_index - 1] == 0:
            depth = depth + 1
            depth_list.append(depth)
    # print(depth_list)
    # print(len(depth_list))
    depth = max(depth_list)
    # print(depth)

    for i in range(len(words)):
        if head[i] != 0:
            child_point = []
            result = []
            father_point = words[head[i] - 1]
            index = i + 1
            for j in range(len(head)):
                if head[j] == index:
                    # 不加words[j]直接加下标
                    child_point.append(j)
            result.append(words[i])
            result.append(child_point)
            result.append(sentence_tree[i])
            result.append(depth_list[i])
            result.append(father_point)
            tree_structure.append(result)
        if head[i] == 0:
            child_point = []
            result = []
            father_point = '自己是根节点'
            index = i + 1
            for j in range(len(head)):
                if head[j] == index:
                    child_point.append(j)
            result.append(words[i])
            result.append(child_point)
            result.append(sentence_tree[i])
            result.append(depth_list[i])
            result.append(father_point)
            tree_structure.append(result)
    # for node in tree_structure:
    #     print(node)

    json_tree = [0 for x in range(0, len(words))]
    leaf_index = []
    for i in range(len(tree_structure)):
        if not tree_structure[i][1]:
            leaf_index.append(i)
            json_tree[i] = {'name': tree_structure[i][0] + ',' + tree_structure[i][2], 'value': 100000}

    not_leaf_node = []
    for i in range(len(tree_structure)):
        if i not in leaf_index:
            not_leaf_node.append(tree_structure[i])
        if i in leaf_index:
            not_leaf_node.append(0)

    for i in range(depth - 1, 0, -1):
        for j in range(len(not_leaf_node)):
            if not_leaf_node[j] != 0 and not_leaf_node[j][3] == i:
                children = []
                for number in not_leaf_node[j][1]:
                    children.append(json_tree[number])
                json_tree[j] = {'name': not_leaf_node[j][0] + ',' + not_leaf_node[j][2], 'children': children}

    # ms = open('D:/json_tree.json', 'w', encoding='utf-8')
    for node in tree_structure:
        if node[4] == '自己是根节点':
            root_node_name = node[0] + ',' + node[2]
    for single_json in json_tree:
        dic = single_json
        if dic["name"] == root_node_name:
            final_result = dic
            break
    # print(final_result)
    # print(type(final_result))

    # data = json.dumps(final_result, ensure_ascii=False)
    # print(data)
    # print(type(data))
    # ms.write(data)
    # for i in range(4):
    #     print(sentence_pattern_dictionary[i + 1])

    # 首先确定句式
    if "children" in final_result.keys():
        sentence_analysis(final_result)
        removed_repeat_svo = []
        for result in final_svo_result:
            if result not in removed_repeat_svo and result["实施者"]["name"] != "":
                removed_repeat_svo.append(result)
            # if result not in removed_repeat_svo:
            #     removed_repeat_svo.append(result)
        print("-------------最终结果为-------------")
        for result in removed_repeat_svo:
            print(result)
        return removed_repeat_svo


# sentence = "中国和印度举行会议"
# seg_list = ansj_tokenize(sentence,
#                          stop_words=None,
#                          stop_natures=None,
#                          custom_words=None,
#                          min_word_length=1, use_nature=False)
seg_list = [['中国', '和', '印度', '举行会议']]

event_extraction(seg_list)
# event_extraction("他需要承认自己输了，也需要祝贺获胜者")
# file = open("E:/find_query.json", 'r', encoding='utf-8')
# line = file.readline()
# text_data = []
# number_line = 0
# start_time = time.time()
# while line:
#     number_line = number_line + 1
#     if number_line > 100:
#         break
#     dic = json.loads(line)
#     content = dic["content"]
#     sentences = split_sentences(content)
#     for sentence in sentences:
#         print(sentence)
#         event_extraction(sentence)
#     print(number_line)
#     print("分析完成")
#     line = file.readline()
# end_time = time.time()
# print("总用时为")
# print(end_time - start_time)
