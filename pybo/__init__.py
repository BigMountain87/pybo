from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# 1. 애플리케이션을 생성하는 코드
# 2. __name__ : 모듈 명이 담깁니다.
# python 파일 자체를 모듈로 사용 가능합니다.
# 결론적 pybo.py에 파일명 들어갑니다.

# config.py파일을 가져오기
import config

# SQLAlchemy, Migrate의 인스턴스 만들기
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    # config 내용을 app.config 추가
    app.config.from_object(config)
    
    # ORM
    # db : SQLAlchemy 객체
    # migrate: Migrate의 객체
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models
    

    # 블루프린트
    from .views import main_views, question_views, answer_views,user_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(user_views.bp)
    return app