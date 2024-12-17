# 필요한 모듈 및 패키지 불러오기
from datetime import datetime  # 현재 날짜와 시간을 다루기 위한 모듈
from flask import Blueprint, url_for, request  
# Flask에서 필요한 클래스와 함수
from werkzeug.utils import redirect  # URL 리다이렉트를 도와주는 함수

from pybo import db  # 데이터베이스 설정을 불러옴
from pybo.models import Question, Answer  # 데이터베이스 모델인 Question, Answer를 불러옴

# 'answer'라는 이름의 Blueprint 객체 생성
# URL 프리픽스를 '/answer'로 설정하여 모든 라우팅이 '/answer' 하위에서 동작하게 함
bp = Blueprint('answer', __name__, url_prefix='/answer')

# '/create/<int:question_id>' 경로에 대한 POST 요청을 처리하는 함수
# 실제로는 prefix 때문에 /answer/create/<int:question_id>,POST
@bp.route('/create/<int:question_id>', methods=('POST',))
def create(question_id):
    """
    특정 질문(Question)에 대한 답변(Answer)을 생성하는 함수
    :param question_id: 답변을 작성할 질문의 ID
    """
    # 해당 ID의 질문을 데이터베이스에서 가져오며, 존재하지 않으면 404 에러 반환
    question = Question.query.get_or_404(question_id)
    
    # POST 요청의 form 데이터에서 'content' 필드의 값을 가져옴
    content = request.form['content']
    
    # 새로운 Answer 객체 생성 (내용과 현재 날짜/시간을 저장)
    answer = Answer(content=content, create_date=datetime.now())
    
    # 해당 질문 객체의 'answer_set'에 새로운 답변 객체를 추가
    question.answer_set.append(answer)
    
    # 데이터베이스에 변경사항 저장 (트랜잭션 커밋)
    db.session.commit()
    
    # 질문 상세 페이지로 리다이렉트 (해당 질문 ID를 URL 파라미터로 전달)
    return redirect(url_for('question.detail', question_id=question_id))
