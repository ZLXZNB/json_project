import xlrd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import font_manager
wb = xlrd.open_workbook('D:/12_25_topic_co/03-17_04-26.xlsx')
sh = wb.sheet_by_name('Sheet1')
my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/simsun.ttc")
final_result = []
for i in range(1, 11):
    array = []
    for j in range(1, 11):
        array.append(sh.cell(i, j).value)
    final_result.append(array)
vectors = TSNE(n_components=3, learning_rate=200).fit_transform(final_result)
print(vectors)
x = []
y = []
z = []
for vector in vectors:
    x.append(vector[0])
    y.append(vector[1])
    z.append(vector[2])
ax1 = plt.axes(projection='3d')
ax1.plot3D(x, y, z, '*')
text = ['疫情中的众生相', '防控部署', '医疗物资保障与基础设施建设', '疫情中的经济', '疫情中的文化传播', '疫情中的民生', '新冠肺炎医治', '疫情中的国际社会', '新冠疫情动态', '疫情中的法制']
for i in range(len(x)):
    ax1.text(x[i], y[i], z[i], text[i], fontsize=12,  fontproperties=my_font)
plt.show()
