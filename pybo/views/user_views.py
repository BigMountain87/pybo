from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.utils import redirect

from pybo.models import db, Question, User


bp = Blueprint('user', __name__, url_prefix='/user')

# 클라이언트
# http://<주소>/user/create_user로 POST 방식 사용
@bp.route('/create_user',methods = ['POST'] )
def create_user():
    # 1. 클라이언트에서 보낸 본문 내용
    # 클라이언트에서 보낸 json 값을 저장
    # request를 사용하려면,
    # 맨 윗쪽에 from flask import request
    data = request.get_json()
    print(f"data : {data}")
    # 각각 username, password, email
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    # 변수에 저장
    # 원래는 username 있는지 확인 & 같은 username이 있는지 확인
    # 원래는 password 있는지 확인
    # 원래는 email 있는지 확인 해야하는데 간단하게 구조를
    # password hash코드로 바꿔서 저장해야함
    # 만들기위해서 생략
    # 2. DB에 username, password, email을 가지고
    # 새로운 데이터를 추가후 완료인지 에러가 발생했는지 확인
    # User라는 클래스를 이용해서 new_user라는 객체를 생성 + 생성하면서 값을 추가
    new_user = User(username=username,password=password,email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message':'User created successfully'}), 201
