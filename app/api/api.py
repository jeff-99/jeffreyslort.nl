__author__ = 'Jeffrey Slort'
from flask import Blueprint, jsonify, redirect, url_for, render_template,session
from app import db

apiBP = Blueprint("api",__name__,template_folder="templates")

@apiBP.route("/")
def index():
    return redirect("/")

@apiBP.route("/<string:sectie>")
def sectie(sectie):
    doc = db.secties.find_one({"sectie":sectie},{"_id":0})
    if doc:
        if doc.get("type") == "overzicht":
            posts = [p for p in db.posts.find({"sectie":sectie})]
            return render_template(doc["template"],posts=posts)
        else:
            return render_template(doc["template"])
    return "er ging iets mis"

@apiBP.route("/test")
def test():
    user = 4
    print session.keys()
    if not session.has_key("user_id"):
        session["user_id"] = user
        return "welkom user 4"
    else:
        return "je bent ingelogd {}".format(session["user_id"])