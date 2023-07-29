from flask import Flask

app=Flask(__name__)

@app.route("/")
def func():
    return "<h1>HELLO, WORLD!<h1>"

@app.route("/1")
def func1():
    return "<h1>HELLO, WORLD!1<h1>"

@app.route("/2")
def func2():
    return "<h1>HELLO, WORLD!2<h1>"

if __name__=="__main__":
    app.run(host = "0.0.0.0")    