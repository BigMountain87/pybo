from flask import Blueprint, render_template
# Flask에서 Blueprint와 render_template을 가져옵니다.
# Blueprint는 플라스크 앱을 모듈화할 수 있도록 도와주는 기능입니다.
# render_template는 HTML 템플릿 파일을 렌더링하기 위해 사용됩니다.

from pybo.models import Question
# pybo 애플리케이션의 models 모듈에서 Question 클래스를 가져옵니다.
# 이 클래스는 데이터베이스 모델로, 질문 데이터를 나타냅니다.

bp = Blueprint('question', __name__, url_prefix='/question')
# 'question'이라는 이름으로 Blueprint 객체를 생성합니다.
# url_prefix는 이 블루프린트의 모든 URL 앞에 '/question'을 붙이도록 설정합니다.

@bp.route('/list/')
def _list():
    # '/list/' 경로에 대해 라우트를 정의합니다.
    # 이 경로로 요청이 들어오면 _list 함수가 실행됩니다.

    question_list = Question.query.order_by(Question.create_date.desc())
    # 데이터베이스에서 Question 객체를 모두 조회하여 생성일(create_date)을 기준으로 내림차순 정렬합니다.
    # 최신 질문이 먼저 나타나도록 설정합니다.

    return render_template('question/question_list.html', question_list=question_list)
    # question/question_list.html 템플릿을 렌더링하고, 정렬된 question_list를 템플릿에 전달합니다.

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    # '/detail/<int:question_id>/' 경로에 대해 라우트를 정의합니다.
    # <int:question_id>는 URL에서 정수형 데이터를 받아옵니다.
    # 이 값은 detail 함수의 매개변수 question_id에 전달됩니다.

    question = Question.query.get_or_404(question_id)
    # 데이터베이스에서 주어진 question_id에 해당하는 Question 객체를 조회합니다.
    # 만약 해당하는 객체가 없으면 404 에러를 반환합니다.

    return render_template('question/question_detail.html', question=question)
    # question/question_detail.html 템플릿을 렌더링하고, 조회한 question 객체를 템플릿에 전달합니다.
