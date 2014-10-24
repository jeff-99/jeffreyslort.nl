__author__ = 'Jeffrey Slort'

from flask import Blueprint, render_template

websiteBP = Blueprint("website",__name__,template_folder="templates")

@websiteBP.route('/')
def index():
    return render_template("index.html", id="yomamma2")

