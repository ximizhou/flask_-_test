from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    data={
        'name':'张三',
        'age':18
    }
    return jsonify(data['name'])

if __name__ == '__main__':
    app.run()