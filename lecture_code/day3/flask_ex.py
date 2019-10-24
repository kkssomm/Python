from flask import Flask
import random
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