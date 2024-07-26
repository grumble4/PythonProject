import pytest

def add(a,b):
    return a+b

# 装饰器
# 分为两组映射 x=1,y=2
# 第一种实现参数化
@pytest.mark.parametrize(['x','y'],[(1,2),(0,3),(1,4)])
def test_add1(x,y):
    assert 3==add(x,y)

# 第二种
xy=[(-1,3),(-1,4),(1,-4)]
@pytest.mark.parametrize(['x','y'],xy)
def test_add2(x,y):
    assert 3==add(x,y)

# 把存储在mysql当中的测试用例参数化出来
import pymysql
db_info={
    "host":"192.168.2.119",
    "user":"root",
    "password":"123",
    "database":"mydb2",
    "charset":"utf8"
}
conn=pymysql.connect(**db_info)
cursor=conn.cursor()
sql="select * from mumu"
cursor.execute(sql)
result=cursor.fetchall()

@pytest.mark.parametrize([
    'id'
])
def test_mysql_param():
    pass

if __name__=="__main__":
    pytest.main(['test_pytest3.py'])