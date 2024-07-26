from flask import Flask,request

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "helloqqq"

@app.route("/hello")
def hello_world2():
    return "hello2222"

@app.route("/hello/<username>")
def hello_world3(username):
    print(username)
    return "hello2222"+username



@app.route("/hello/args/<username>")
def hello_world4(username):
    print(username)
    key=request.args.get("key")
    value=request.args.get("value")
    print(key)
    print(value)
    return "hello22222"+ username+":::"+key+value

if __name__ == "__main__":
    app.run()