from flask import Flask

app = Flask(__name__)

# This is a Hello World Code!!
@app.route('/')
def hello_world():
    return 'Hello, Payppy! :)'

@app.route('/Addtion')
def Addition(num:a, num:b)->num:
    a = 4
    b = 5
    return  a+b   



