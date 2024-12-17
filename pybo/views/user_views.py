from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.utils import redirect

from pybo.models import db, Question, User

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/user_list',methods=['GET'])
def user_list():
    # 1. 전체 사용자 데이터를 가져오기
    users = User.query.all()
    
    # 2. 가져온 데이터 JSON 형태로 변환
    user_list = [] # 비어있는 리스트 배열 추가
    for  user in users:
        user_list.append({
            'id': user.id,
            'username' : user.username,
            'email' : user.email
        })

    # 3. 클라이언트에 출력 return
    return jsonify(user_list)



#http://127.0.0.1:5000/user/delete_user/<id>
@bp.route('/delete_user/<int:id>',methods=['DELETE'])
def delete_user(id):
    # 1. id로 DB를 조회해서 존재하는지 확인
    # User를 id로 query를 한 후 user라는 변수 저장
    user = User.query.get(id)

    if not user:
        return jsonify({"message":f"ID {id}인 사용자가 존재하지 않습니다."}), 404
    # 2. DB에서 id에 해당하는 자료를 삭제
    
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message":f"사용자 ID {id}가 성공적으로 삭제되었습니다."}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message":"사용자 삭제중 에러가 발생했습니다.","error":str(e)}), 500
    # 3. 삭제된 결과를 메시지 전송

    # try, except 구문
    # 어떤 작업을 실행 에러가나면 except 구문을 실행
    # 예) DB에 삭제를 했는데 에러가 나면 except구문에 에러코드를 보여줌


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
