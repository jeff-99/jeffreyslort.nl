__author__ = 'Jeffrey Slort'

from flask import Flask, redirect, url_for,g,current_app
from flask.ext.mongokit import MongoKit
from flask.ext.mail import Mail
from blog.models import Post
from frontend.models import Sectie
from datetime import datetime
from mongosessions import MongoSessionInterface

app = Flask(__name__)
app.config.from_pyfile("config.py")

db = MongoKit(app)
db.register([Post,Sectie])

mailer = Mail(app)

from api.api import apiBP
from frontend.views import websiteBP
from blog.views import blogBP
app.register_blueprint(websiteBP,url_prefix="")
app.register_blueprint(apiBP,url_prefix="/api")
app.register_blueprint(blogBP,url_prefix="/blog")
app.jinja_env.globals.setdefault("datetime",datetime)

app.session_interface = MongoSessionInterface(db_connection=db)