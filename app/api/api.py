__author__ = 'Jeffrey Slort'
from flask import Blueprint, jsonify, redirect, url_for, render_template,session
from app import db

apiBP = Blueprint("api",__name__,template_folder="templates")

@apiBP.route("/")
def index():
    return redirect("/")


@apiBP.route("/test")
def test():
    user = 4
    print session.keys()
    if not session.has_key("user_id"):
        session["user_id"] = user
        return "welkom user 4"
    else:
        return "je bent ingelogd {}".format(session["user_id"])