from flask import Blueprint, render_template
from app.models import Question


                # 우리가 부를 이름, flask 프레임워크가 찾을 이름, 라우팅주소
fisa = Blueprint('basic', __name__, url_prefix='/fisa')

@fisa.route('/about_me')
def about_me():
    return f"저는 {__name__}입니다."

@fisa.route('/hello')
def hello():
    return "안녕하세요"

@fisa.route('/bye')
def bye():
    return "잘가세요"


# basic_views.soie 
                # 우리가 부를 이름, flask 프레임워크가 찾을 이름, 라우팅주소
soie = Blueprint('soie', __name__, url_prefix='/soie')

@soie.route('/about_me')
def about_me():
    return f"저는 {__name__}입니다."

@soie.route('/hello')
def hello():
    return "안녕하세요"

@soie.route('/bye')
def bye():
    return "잘가세요"

@fisa.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get(question_id)
    return render_template('question/question_detail.html', question=question)

@fisa.route('/post')
def post_list():
    return 'question\question_list.html'
