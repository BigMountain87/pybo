from flask import Blueprint, render_template

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    # DB에서 쿼리로 조회 나온 결과를 question_list에 저장
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)
                                                           # 매개변수명 = DB에서조회한 결과
# http://localhost:5000/detail/2/ 응답요청
# URL 라우팅: '/detail/<int:question_id>/'에 요청이 오면 이 함수가 실행됨
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    # 데이터베이스에서 주어진 question_id에 해당하는 질문 데이터를 조회
    # Question은 데이터베이스 모델로, query.get()을 통해 해당 ID의 레코드를 가져옴
    question = Question.query.get_or_404(question_id)
    
    # 조회된 질문 데이터를 question_detail.html 템플릿에 전달하여 렌더링
    # 'question' 변수로 템플릿에서 사용할 수 있게 전달
    return render_template('question/question_detail.html', question=question)
