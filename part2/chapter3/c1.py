import pandas as pd

# 显示所有的列
pd.set_option('display.max_columns',None)
# 显示所有的行
pd.set_option('display.max_rows',None)
# 获取Excel中的数据
sheet1_data=pd.read_excel("接口自动化测试用例.xlsx")
print(sheet1_data)