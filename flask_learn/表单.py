from flask import Flask, render_template, request
import os
root_dir = os.path.dirname(__file__)
files = os.path.join(root_dir, '..')
app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html', files=files)

if __name__ == '__main__':
    app.run()