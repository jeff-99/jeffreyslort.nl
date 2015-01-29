__author__ = 'Jeffrey Slort'

from datetime import datetime

from flask import Flask, g
from flask.ext.mongokit import MongoKit
from flask.ext.mail import Mail
from flask.ext.login import LoginManager

from blog.models import Post
from admin.models import User
from frontend.models import Sectie
from app.auth.mongosessions import MongoSessionInterface


app = Flask(__name__)
app.config.from_pyfile("config.py")

db = MongoKit(app)
db.register([Post,Sectie,User])

mailer = Mail(app)

login_manager = LoginManager(app)
login_manager.login_view = "admin.login"
login_manager.id_attribute = "get_id"
@login_manager.user_loader
def load_user(id):
    user = db.User.get_from_id(id)
    g.user = user
    return user


from api.api import apiBP
from frontend.views import websiteBP
from blog.views import blogBP
from admin.views import adminBP
app.register_blueprint(websiteBP,url_prefix="")
app.register_blueprint(apiBP,url_prefix="/api")
app.register_blueprint(blogBP,url_prefix="/blog")
app.register_blueprint(adminBP,url_prefix="/admin")
app.jinja_env.globals.setdefault("datetime",datetime)
app.jinja_env.globals.update(hasattr=hasattr)
app.session_interface = MongoSessionInterface(db_connection=db)