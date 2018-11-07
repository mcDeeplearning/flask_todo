from flask import Flask, render_template, request, redirect
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
    todos = Todo.query.order_by(Todo.deadline.asc()).all()
    return render_template('index.html',todos=todos)
    
# @app.route('/posts/new')
# def new():
#     return render_template('new.html')
    
# @app.route('/posts/create', methods=['POST'])
# def create():
#     # 사용자가 입력한 데이터 가져오기
#     todo = request.form['todo']
#     deadline = request.form.get('deadline')
#     # 가져온 데이터로 Todo 만들기
#     todo = Todo(todo,deadline)
#     # ToDo DB에 저장하기
#     db.session.add(todo)
#     db.session.commit()
#     # 어느 페이지로 이동할지 정하기
#     return redirect('/')

@app.route('/todos/create', methods=['POST','GET'])
def todo():
    if request.method == "POST":
        todo = Todo(request.form['todo'],request.form['deadline'])
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
        
    return render_template('new.html')
    
# 삭제하는 경로를 라우트에 추가한다.
@app.route('/todos/<int:id>/delete')
def delete(id):
    # 몇번글을 삭제할지 알아낸다?
    todo = Todo.query.get(id)
    # 글을 삭제한다.
    db.session.delete(todo)
    # 상태를 저장한다.
    db.session.commit()
    # 어디로 보낼지(url) 설정한다. 
    return redirect('/')

# EDIT 처리 로직
# EDIT하는 경로를 라우트에 추가한다.
@app.route('/todos/<int:id>/edit')
def edit(id):
    # 기존의 데이터를 가져와서 수정할수 있는 폼 보여주기
    todo = Todo.query.get(id)
    return render_template('edit.html',todo=todo)

# UPDATE 처리 로직
# UPDATE하는 경로를 라우트에 추가한다.
@app.route('/todos/<int:id>/update', methods=["POST"])
def update(id):
    # 변경한 데이터를 가져와서 db에 반영
    todo = Todo.query.get(id)
    todo.todo = request.form['todo']
    todo.deadline = request.form['deadline']
    
    db.session.commit()
    
    return redirect('/')





    