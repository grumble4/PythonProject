import pandas as pd

# 显示所有的列
pd.set_option('display.max_columns',None)
# 显示所有的行
pd.set_option('display.max_rows',None)
# 获取Excel中的数据
sheet1_data=pd.read_excel("../接口自动化测试用例.xlsx")

# 数据的筛选访问
login_case_type=sheet1_data[sheet1_data["请求接口类别"]=="登录"]
print(login_case_type)

# json(字典)数据解析
login_case_data=login_case_type['输入数据'][0]
print(login_case_data)
print(type(login_case_data))

import json
login_case_data_dict=json.loads(login_case_data)
print(login_case_data_dict)
print(type(login_case_data_dict))
username=login_case_data_dict['userName']
password=login_case_data_dict['password']
print(username)
print(password)
