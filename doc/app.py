# -*- coding: utf-8 -*-
from functools import reduce

from flask import Flask,render_template,request,redirect,url_for,flash

from werkzeug.routing import BaseConverter
from os import path

from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from flask_sqlalchemy import SQLAlchemy

basedir = path.abspath(path.dirname(__file__))

class RegexConverter(BaseConverter):
    def __init__(self,url_map,*items):
        super(RegexConverter,self).__init__(url_map)
        self.regex=items[0]

bootstrap = Bootstrap()
nav = Nav()
db=SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.url_map.converters['regex'] = RegexConverter

    #读取配置文件
    app.config.from_pyfile('config')

    #sqlite
    app.confg['SQLALCHEMY_DATABASE_URI']='sqlite:///'+path.join(basedir,'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

    bootstrap.init_app(app)
    nav.init_app(app)
    db.init_app(app)

    nav.register_element('top', Navbar('Flask入门',
                                       View('主页', 'index'),
                                       View('关于', 'about'),
                                       View('服务', 'services'),
                                       View('项目', 'projects'),
                                       ))



# if __name__ == '__main__':
    # app.run(debug=True)
    # manager.run()

    # app.debug = True
    # server = Server(app.wsgi_app)
    # server.serve()