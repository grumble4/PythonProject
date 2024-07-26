import pymysql
from flask import Flask

# 这里是mysql的基本连接信息
conn =pymysql.connect(
    host="10.125.25.144",
    user="root",
    password="123",
    database="mydb1",
    charset="utf8"
)

cursor=conn.cursor()

app=Flask(__name__)

@app.route("/")
def hello_world():
    sql ="select * from user"
    result=cursor.execute(sql)
    # 得到查询后的真正结果
    r=cursor.fetchall()
    print(r)
    return str(r)

if __name__ == "__main__":
    app.run()