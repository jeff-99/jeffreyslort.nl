__author__ = 'Jeffrey Slort'
from flask import Blueprint, jsonify, redirect, url_for, render_template
from app import db

apiBP = Blueprint("api",__name__,template_folder="templates")

@apiBP.route("/")
def index():
    return redirect("/")

@apiBP.route("/<string:sectie>")
def sectie(sectie):
    doc = db.secties.find_one({"sectie":sectie},{"_id":0})
    return render_template(doc["template"],properties=doc["properties"])
