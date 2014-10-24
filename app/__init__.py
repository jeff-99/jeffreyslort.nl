__author__ = 'Jeffrey Slort'

from flask import Flask, redirect, url_for,g
from flask.ext.mongokit import MongoKit
from blog.models import Post

app = Flask(__name__)
app.config.from_pyfile("config.py")

db = MongoKit(app)
db.register([Post])



from api.api import apiBP
from frontend.views import websiteBP
from blog.views import blogBP
app.register_blueprint(websiteBP,url_prefix="/index")
app.register_blueprint(apiBP,url_prefix="/api")
app.register_blueprint(blogBP,url_prefix="/blog")

