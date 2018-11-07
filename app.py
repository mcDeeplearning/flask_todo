from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import *

app = Flask(__name__)

# db설정
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///todo'
# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db.init_app(app)
migrate = Migrate(app,db)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/posts/new')
def new():
    return render_template('new.html')
    
@app.route('/posts/create')
def create():
    # 사용자가 입력한 데이터 가져오기
    # 가져온 데이터로 Todo 만들기
    # ToDo DB에 저장하기
    # 어느 페이지로 이동할지 정하기
