from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    data={
        'name':'张三',
        'age':18
    }
    return render_template('index2.html',data=data)

if __name__ == '__main__':
    app.run()