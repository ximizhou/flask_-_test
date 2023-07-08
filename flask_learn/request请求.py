from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
        # return 'nihao'
    if request.method=='POST':
        name=request.form.get('name')
        password=request.form.get('password')
        print(name,password)
        return 'success'
        # return (name ,password),这个不可以
        # return render_template('index2.html')

if __name__ == '__main__':

    app.run(debug=True)




