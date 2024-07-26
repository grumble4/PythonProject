from flask import Flask,request

app=Flask(__name__)

@app.route("/mypost",methods=["post"])
def my_post():
    return "post request"

@app.route("/mypost1",methods=["post"])
def my_post1():
    #表单数据类型
    username=request.form["username"]
    sex=request.form["sex"]
    print(username)
    print(sex)
    return "post request" + username + "::" +sex

@app.route("/mypost1",methods=["post"])
def my_post2():
    #json数据格式
    request_data=request.get_json()
    print(request_data["user"])
    return "post request" + str(request_data)

if __name__=="__main__":
    app.run(port=5555)