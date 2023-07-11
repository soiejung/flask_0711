from flask import Flask


def create_app():
    # 따로 set FLASK_APP=파일명 적어주지 않으면 app.py를 기본 실행 입구로 찾습니다.
    app = Flask(__name__)

    from .views import basic_views, soie_views
    app.register_blueprint(basic_views.fisa)
    app.register_blueprint(soie_views.soie)
    return app