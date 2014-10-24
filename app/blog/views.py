__author__ = 'Jeffrey Slort'

from flask import Blueprint, redirect, url_for,jsonify, render_template
from app import db

blogBP = Blueprint("blog",__name__)

@blogBP.route("/")
def index():
    return redirect(url_for("blog.overzicht"))

@blogBP.route("/overzicht", defaults={"pagina": 0})
@blogBP.route("/overzicht/<int:pagina>")
def overzicht(pagina):
    skip = pagina * 5
    posts = []
    for post in db.Post.find({},{"_id":0}).limit(5).skip(skip):
        posts.append(post)
    return render_template("overzicht.html", posts=posts)



@blogBP.route("/<int:jaar>/<string:titel>")
def post(jaar,titel):
    return (str(jaar) + titel)

@blogBP.route("/permalink/<string:hash>")
def perma(hash):
    return "permalinks"