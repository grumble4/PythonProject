import pandas as pd

# 显示所有的列
pd.set_option('display.max_columns',None)
# 显示所有的行
pd.set_option('display.max_rows',None)
# 获取Excel中的数据
sheet1_data=pd.read_excel("../接口自动化测试用例.xlsx")
sheet2_data=pd.read_excel("../接口自动化测试用例.xlsx",sheet_name="案例数据")
# print(sheet2_data)
print(sheet2_data)
print(type(sheet1_data))
# 单独访问一列的数据
print("*"*20+"访问列数据"+"*"*10)
print(sheet1_data['编号'])
print(type(sheet1_data['编号']))

print(sheet1_data[['编号','标题']])

print("*"*10+"访问列数据后再访问行的数据"+"*"*10)
print(sheet1_data['编号'][0])
print(sheet1_data[['编号','标题']][1:4])

print("*"*10+"单独访问行的数据"+"*"*10)
print(sheet1_data.iloc[[1]])
# print(sheet1_data.iloc[[1,2,3],[1,2]])
print(sheet1_data.iloc[0:2,0:4])

