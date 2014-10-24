__author__ = 'Jeffrey Slort'
from flask import Blueprint, jsonify, redirect, url_for
from models import pimpie

apiBP = Blueprint("api",__name__)

@apiBP.route("/")
def index():
    return redirect("/")

@apiBP.route("/<string:sectie>")
def sectie(sectie):

    doc = {"id": sectie}

    return jsonify(doc)