from ddparser import DDParser
from LAC import LAC
import xlsxwriter
import json

sentence_pattern_dictionary = {1: "主谓宾", 2: "主谓", 3: "对字句", 4: "把字句", 5: "被字句"}


def string_to_list(a):
    if a.split(','):
        return a.split(',')
    else:
        return [a]


def judgment_sentence_pattern(result_dictionary):
    sentence_pattern = 1
    children_list = result_dictionary["children"]
    for dictionary in children_list:
        name_list = string_to_list(dictionary["name"])
        name = name_list[0]
        relationship = name_list[1]
        if name == "对" and relationship == "ADV":
            sentence_pattern = 2
            break
        else:
            if relationship == "POB":
                if name == "把":
                    sentence_pattern = 3
                    break
                if name == "被":
                    sentence_pattern = 4
                    break
    return sentence_pattern


lac = LAC(mode='lac')
ddp = DDParser()
sentence = "铜川"
# lac_result = lac.run(sentence)
analysis_result = ddp.parse(sentence)
print(analysis_result)
# ner_result = lac_result[1]
number = 0
per_number = []
# for entity in ner_result:
#     if entity == 'PER':
#         per_number.append(number)
#         number = number + 1
#     if entity != 'PER':
#         number = number + 1
print(analysis_result)
words = analysis_result[0]["word"]
head = analysis_result[0]["head"]
sentence_tree = analysis_result[0]["deprel"]
tree_structure = []
print(words)
print(head)

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
print(depth_list)
print(len(depth_list))
depth = max(depth_list)
print(depth)

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
for node in tree_structure:
    print(node)

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

ms = open('D:/json_tree.json', 'w', encoding='utf-8')
for node in tree_structure:
    if node[4] == '自己是根节点':
        root_node_name = node[0] + ',' + node[2]
for single_json in json_tree:
    dic = single_json
    if dic["name"] == root_node_name:
        final_result = dic
        break
print(final_result)
print(type(final_result))

data = json.dumps(final_result, ensure_ascii=False)
print(data)
print(type(data))
ms.write(data)

sentence_pattern_dictionary = {1: "经典主谓", 2: "对字句", 3: "把字句", 4: "被字句"}
# for i in range(4):
#     print(sentence_pattern_dictionary[i + 1])

# 首先确定句式
sentence_pattern_type = judgment_sentence_pattern(final_result)

# 根据句式选择不同的方法
