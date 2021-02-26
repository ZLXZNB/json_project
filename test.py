# mystr = input("请输入一个字符串:")
# isallEng = True
# for i in mystr:
#     if (i.upper() > 'Z' or i.upper() < 'A'):
#         isallEng = False
#         break
# if (isallEng):
#     print("全是英文")
# else:
#     print("不全是英文")

# seg = [['是大家安静','打开速度','打算看到你看'],['大数据','的撒看到你']]
# seg[0].remove('打开速度')
# print(seg)
# print('返回'.encode('utf-8').isalpha())

def containenglish(str0):
    import re
    return bool(re.search('[a-z]', str0))
print(containenglish('防疫'))