# -*- coding: utf-8 -*-

from flask import Flask

from werkzeug.routing import BaseConverter
from os import path

from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from flask_sqlalchemy import SQLAlchemy
# from app.main.views import init_views
from flask_login import LoginManager

class RegexConverter(BaseConverter):
    def __init__(self,url_map,*items):
        super(RegexConverter,self).__init__(url_map)
        self.regex=items[0]

basedir = path.abspath(path.dirname(__file__))
bootstrap = Bootstrap()
nav = Nav()
db=SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'

def create_app():
    app = Flask(__name__)
    app.url_map.converters['regex'] = RegexConverter

    #读取配置文件
    app.config.from_pyfile('config')

    #sqlite
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+path.join(basedir,'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
    nav.register_element('top', Navbar('Flask入门',
                                       View('主页', 'main.index'),
                                       View('关于', 'main.about'),
                                       View('服务', 'main.services'),
                                       View('项目', 'main.projects'),
                                       ))

    bootstrap.init_app(app)
    nav.init_app(app)
    db.init_app(app)
    # init_views(app)
    login_manager.init_app(app)

    from app.auth import auth as auth_blueprint
    from app.main import main as main_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(main_blueprint, url_prefix='/main')
    return app




# if __name__ == '__main__':
    # app.run(debug=True)
    # manager.run()

    # app.debug = True
    # server = Server(app.wsgi_app)
    # server.serve()