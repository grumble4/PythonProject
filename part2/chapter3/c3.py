import pandas as pd

# 显示所有的列
pd.set_option('display.max_columns',None)
# 显示所有的行
pd.set_option('display.max_rows',None)
# 获取Excel中的数据
sheet1_data=pd.read_excel("../接口自动化测试用例.xlsx")

# 把所有列的值，依此取出来
# for i in sheet1_data:
#     print(i)
#     print(sheet1_data[i])

# 按照行来进行依次的数据访问
# for i in sheet1_data.index:
#     print(i)
#     print(sheet1_data.iloc[i])

# i行索引
# 访问Excel中每一个单元格中的数据
for i in sheet1_data.index:
    for j in sheet1_data.iloc[[i]]:
        print(sheet1_data[j][i])