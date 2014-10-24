__author__ = 'Jeffrey Slort'

from flask import Flask, redirect, url_for,g
from flask.ext.mongokit import MongoKit
from flask.ext.mail import Mail
from blog.models import Post
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile("config.py")


db = MongoKit(app)
db.register([Post])

mailer = Mail(app)

from api.api import apiBP
from frontend.views import websiteBP
from blog.views import blogBP
app.register_blueprint(websiteBP,url_prefix="/index")
app.register_blueprint(apiBP,url_prefix="/api")
app.register_blueprint(blogBP,url_prefix="/blog")
app.jinja_env.globals.setdefault("datetime",datetime)

