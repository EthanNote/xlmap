import flask
from flask import render_template

app=flask.Flask(__name__)

@app.route('/')
def view():
    return render_template('view.html')

@app.route('/data.json')
def data():
    f=open('data.json','r')
    content=f.read()
    f.close()
    return content

app.run()