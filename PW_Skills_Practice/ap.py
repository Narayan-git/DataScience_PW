from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<H1> Hello World<br> welcome to Python API</H1>"

# for taking input from url
@app.route("/TakeInput")
def request_input():
    data = request.args.get('value')
    return "This is our API input value {}".format(data)

if __name__ =="__main__":
    app.run(host ="0.0.0.0")
