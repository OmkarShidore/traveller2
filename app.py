from flask import Flask, render_template, make_response, request
import json
from markupsafe import escape
import time

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Index Page</p>"

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route("/owner")
def owner():
    resp = {
        "username": "omkar",
        "theme": "shidore",
        "image": "lol there's no image"
    }
    return resp, 200


@app.route("/square", methods=['GET'])
def square():
    time.sleep(10)
    num = float(request.args.get("num"))
    return json.dumps(num*num)

@app.route("/power", methods=["GET"])
def power():
    time.sleep(10)
    num = float(request.args.get("num"))
    power_to = float(request.args.get("power_to"))
    ans = num**power_to
    return json.dumps(ans)

if __name__ == '__main__':
    #app.run(port=8080)
    app.run(host='0.0.0.0', port=8080)
    #app.run(port=5000, debug=True)