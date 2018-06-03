#锁定包版本
pip freeze > requirements.txt

#安装指定版本的包列表，可以批量安装依赖
pip install -r requirements.txt

##livereload

##autoescape

##过滤器、自定义过滤器

##block

##include界面

##macro

##从models创建sqlite数据库
```
python manager.py shell
>>> from app import db
>>> from app import models
>>> db.create_all()
>>> from app.models import Role,User
>>> admins=Role(name='administrators')
>>> mod=Role(name='moderator')
>>> db.session.add_all([admins,mod])
>>> db.session.commit()
>>> hx=User(name='hx',role=admins)
>>> db.session.add(hx)
>>> db.session.commit()
>>> hx.password='123456'
>>> db.session.add(hx)
>>> db.session.commit()
>>> db.session.delete(hx)
>>> db.session.commit()
>>> db.session.add(User(name='hx',role=admins))
>>> db.session.commit()
>>> User.query.all()
[<User 1>]
>>> User.query.get(1)
<User 1>
>>> User.query.get(1).name
'hx'
>>> Role.query.count()
2
>>> Role.query.filter('id>0')
<flask_sqlalchemy.BaseQuery object at 0x000000FE83F73240>
```