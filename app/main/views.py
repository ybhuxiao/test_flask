
from os import path
from functools import reduce
from flask import render_template,request,flash,redirect,url_for

from werkzeug.utils import secure_filename
from . import main

@main.route('/')
def index():
    return render_template('index.html', title='Welcome<br /><br /><br /><br />', body='###title')

@main.route('/services')
def services():
    return 'Services'

@main.route('/about')
def about():
    return 'About'

#int, float, path
@main.route('/user/<int:username>')
def user(username):
    return 'User %s'%username

#url使用正则
@main.route('/u/<regex("[a-z]{3}"):username>')
def u(username):
    return 'User %s'%username

@main.route('/projects/')
@main.route('/our-works')
def projects():
    return 'The project page'

@main.route('/upload',methods=['GET','POST'])
def upload():
    if(request.method=='POST'):
        f = request.files['file']
        basepath = path.abspath(path.dirname(__file__))
        upload_path=path.join(basepath,'static','uploads')
        filepath = path.join(upload_path,secure_filename(f.filename))
        print(filepath)
        f.save(filepath)

        return redirect(url_for('upload'))
    return render_template('upload.html')

@main.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


#新增过滤器：markdown转html
# @main.template_filter('md')
# def markdown_to_html(txt):
#     from markdown import markdown
#     return markdown(txt)


def read_md(filename):
    with open(filename) as md_file:
        content=reduce(lambda x,y:x+y,md_file.readlines())
    return content.encode().decode('utf-8')

@main.context_processor
def inject_methods():
    return dict(read_md=read_md)

# @main.template_test('current_link')
# def is_current_link(link):
#     is_curr = link == request.path
#     print(link,is_curr)
#     return is_curr
