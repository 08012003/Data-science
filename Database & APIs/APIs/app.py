from flask import Flask

# request: Used to get input from the URL.
from flask import request

app = Flask(__name__)


# When the root URL (/) is accessed, it runs the hello_world function and returns "Hello, World!" as an HTML heading.
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


# @app.route("/hello_world1") and @app.route("/hello_world2"): Similar to the root URL, 
# but with different paths (/hello_world1 and /hello_world2) and different messages.

@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello, World!1</h1>"


@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello, World!2</h1>"

@app.route("/test")
def test():
    a = 5+6 
    return "this is my function to run app {}".format(a)


# Accepts a input parameter x from the URL and displays it in the message. 
# Example: If accessed as /test2/test2?x=aniket, it will show "this is a data input form my url aniket"

@app.route("/test2/test2")
def test2():
    data = request.args.get('x')
    return  "this is a data input form my url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
