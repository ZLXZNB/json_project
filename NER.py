from LAC import LAC

# 装载LAC模型
lac = LAC(mode='lac')

# 单个样本输入，输入为Unicode编码的字符串weiyang
text = "孙校长当上主席"
lac_result = lac.run(text)
print(lac_result)
