from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return "<h1>Testing.</h1><p>aaa</p>"

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=""):
    return render_template("hello.html")

@app.route('/greet', methods = ['POST'])
def greet():
    typed_name = request.form['name']
    return render_template("hello.html", name=typed_name)

@app.route('/add')
def add():
    first_number = request.args.get('first', '')
    second_number = request.args.get('second', '')
    if first_number and second_number:
        try:
            result = int(first_number) + int(second_number)
        except ValueError:
            return 'invalid data'
        return f'{first_number} + {second_number} = {result}'
    else:
        return 'no args detected'

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9008, debug=True)
