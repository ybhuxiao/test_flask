
from os import path
from functools import reduce
from flask import render_template,request,flash,redirect,url_for

from werkzeug.utils import secure_filename
from .import auth
from flask_login import login_user,logout_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method=='POST':
    #     username=request.form['username']
    #     password=request.form['password']
    #     print(username,password)
    # else:
    #     #http://127.0.0.1:5000/login?username=ray
    #     username = request.args['username']
    #     print(username)
    # return render_template('login.html',method=request.method)

    from app.auth.forms import LoginForm
    from app.models import User
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data,password=form.password.data).first()
        if(user is not None):
            login_user(user)
            return redirect(url_for('main.index'))
    # flash(u'登录成功')
    return render_template('login.html', title='登录', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    from app.auth.forms import RegistrationForm
    form = RegistrationForm()

    from app.models import User
    if(form.validate_on_submit()):
        user = User(email=form.email.data,
                    name=form.username.data,
                    password=form.password.data)

        from app import db
        db.session.add(user)
        db.session.submit()
        return redirect(url_for('auth.login'))

    return render_template('register.html', title=u'注册', form=form)