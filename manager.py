from werkzeug.utils import secure_filename
from flask_script import Manager
from livereload import Server,shell
from app import create_app,db
from flask_migrate import Migrate,MigrateCommand,upgrade

app=create_app()
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command
def dev():
    server = Server(app.wsgi_app)
    server.watch('**/*.*')
    server.serve(open_url=True)

@manager.command
def test():
    pass

@manager.command
def deploy():
    from app.models import Role
    upgrade()
    Role.seed()

if __name__ == '__main__':
    # manager.run()
    dev()
