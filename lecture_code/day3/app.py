from flask import Flask, render_template, request
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/sparta')
def sparta():
    return "This is sparta"

@app.route("/greeting/<string:name>")
def greeting(name):
    return f'반갑습니다! {name}님'

@app.route('/cube/<int:num>')
def cube(num):
    result = num**3 #num*num*num
    return f'{num}의 세제곱은 {result}'

@app.route("/dinner/<int:person>")
def dinner(person):
    menu = ['짜장면','짬뽕','볶음밥','고추잡채밥','마파두부밥']
    order = random.sample(menu,k=person)
    return str(order)

@app.route("/d_day")
def d_day():
    today = datetime.datetime.now()
    finish = datetime.datetime(2019,11,27)
    remain = finish - today
    return f'끝나는 날까지 {remain}일 남았다'

@app.route("/naver")
def naver():
    return render_template("naver.html")

@app.route("/google")
def google():
    return render_template("google.html")

@app.route('/myday')
def myday():
    today = datetime.now()
    return render_template('myday.html', today=today)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    name = request.args.get('name')
    age = request.args.get('age')
    return render_template('pong.html', name=name, age=age)

@app.route('/ping2')
def ping2():
    return render_template('ping2.html')

@app.route('/pong2')
def pong2():
    name = request.args.get('name')
    stats = ['천사','순수','성실','건전','정상']
    return render_template('pong2.html',name=name,stats=random.sample(stats,1))