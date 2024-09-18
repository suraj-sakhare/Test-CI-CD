from flask import Flask

app = Flask(__name__)

# This is a Hello World Code!!
@app.route('/')
def hello_world():
    return 'Hello, Payppy! :)'

@app.route('/addition')
def Addition()->str:
    a = 4
    b = 5
    ans = a+b
    return  'The Sum Sum of {a} and {b} is {ans}'   



