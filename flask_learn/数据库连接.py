from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_migrate import Migrate
query_str=text("select 1;")
app = Flask(__name__)

HOSTNAME='127.0.0.1'
PORT='3306'
USERNAME='root'
PASSWORD='123456'
DATABASE='database_learn'

app.config['SQLALCHEMY_DATABASE_URI']=f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"


db=SQLAlchemy(app)

migration = Migrate(app, db)



# #测试
# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(query_str)
#         print(rs.fetchone())

#建立表
class User(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(50),nullable=False)
    password=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(50),nullable=False)

# user=User(username='张三',password='123456')

# with app.app_context():
#     db.create_all()

#ORM模型映射成表的三步
#1.flask db init:这步只需要执行一次
#2.flask db migrate：识别ORM模型的改变，生成迁移脚本
#3.flask db upgrade:运行迁移脚本，同步到数据库中

#解决方案：
#$env:FLASK_APP='realproject'
# $env:FLASK_ENV = "development"


@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/add_user')
def add_user():
    user=User(username='张三',password='123456')
    db.session.add(user)
    db.session.commit()
    return 'success'

@app.route('/query_user')
def query_user():
    user=User.query.filter_by(username='张三').first()
    print(user)
    return 'success'



if __name__ == '__main__':
    app.run()