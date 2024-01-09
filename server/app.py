#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

app.route('/print/<string:input>')
def print_string(input):
    print(input)
    return f'<p>{input}</p>'

app.route('/count/<integer:input>')
def count(input):
    for each in range(input):
        print(each)

app.route('math/<num1><operation><num2>')
def math(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "div":
        return num1 / num2
    elif operation == "%":
        return num1 % num2
    else:
        print("enter valid operator")


if __name__ == '__main__':
    app.run(port=5555, debug=True)
