import flask
from flask import render_template
from flask import make_response
from flask import jsonify
from mapdata import *

app = flask.Flask(__name__)


@app.route('/')
def view():
    return render_template('view.html')


# @app.route('/data.json')
# def data():
#     f = open('data.json', 'r')
#     content = f.read()
#     f.close()
#     return content


@app.route('/data.json')
def mapjson():
    # return "hello"
    data=getdata()
    # print(data)
    response = make_response(jsonify(response=getdata()))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


app.run(debug=True)
