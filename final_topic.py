import xlrd
import xlsxwriter

wb = xlrd.open_workbook('D:/final_topic.xlsx')
sh = wb.sheet_by_name('Sheet1')
workbook = xlsxwriter.Workbook('D:/final_topic_new.xlsx')  # 建立文件
worksheet = workbook.add_worksheet(
    'Sheet1')  # 建立sheet， 可以work.add_worksheet('employee')来指定sheet名，但中文名会报UnicodeDecodeErro的错误
print(sh.cell(1, 1).value)  # 输出第一行第一列的值
print(sh.ncols)  # 有效数据列数

for i in range(1, 189):
    worksheet.write(1, i, sh.cell(27, i).value)
    worksheet.write(2, i, sh.cell(2, i).value + sh.cell(15, i).value + sh.cell(34, i).value)
    worksheet.write(3, i, sh.cell(13, i).value + sh.cell(21, i).value + sh.cell(29, i).value)
    worksheet.write(4, i, sh.cell(12, i).value + sh.cell(18, i).value)
    worksheet.write(5, i,
                    sh.cell(5, i).value + sh.cell(7, i).value + sh.cell(23, i).value + sh.cell(28, i).value + sh.cell(32, i).value + sh.cell(33, i).value)
    worksheet.write(6, i, sh.cell(9, i).value + sh.cell(19, i).value + sh.cell(25, i).value + sh.cell(26, i).value + sh.cell(36, i).value)
    worksheet.write(7, i, sh.cell(1, i).value + sh.cell(4, i).value + sh.cell(16, i).value + sh.cell(17, i).value + sh.cell(30, i).value)
    worksheet.write(8, i,
                    sh.cell(3, i).value + sh.cell(10, i).value + sh.cell(11, i).value + sh.cell(14, i).value + sh.cell(35, i).value + sh.cell(37, i).value)
    worksheet.write(9, i, sh.cell(8, i).value + sh.cell(20, i).value + sh.cell(22, i).value)
    worksheet.write(10, i,
                    sh.cell(38, i).value + sh.cell(48, i).value + sh.cell(39, i).value + sh.cell(40, i).value + sh.cell(46, i).value + sh.cell(45,
                                                                                                                 i).value + sh.cell(
                        44, i).value + sh.cell(43, i).value + sh.cell(50, i).value)
    worksheet.write(11, i, sh.cell(24, i).value + sh.cell(31, i).value)

#
# worksheet.write(1,1, 'Hello world')  # 向A1写入
#
workbook.close()
