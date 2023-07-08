from flask import Flask
app = Flask(__name__)

@app.route('/<id>')
def hello_world(id):
    if id=='1':
        return 'Hello, World!'
    else:
        return 'Hello, World!'

app.run()
