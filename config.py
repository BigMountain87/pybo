# 데이터베이스와 연결하는 작업
import os

BASE_DIR = os.path.dirname(__file__)
# SQLALCHEMY_DATABASE_URI = 데이터 베이스 접속 주소
# sqlite -> DB 파일형태로 저장
# MySQL, OracleDB -> 서버 형태, 접속
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False # 이벤트를 처리하는 옵션, false
# 홈디렉터리 pybo.db로 데이터베이스가 저장됨