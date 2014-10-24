__author__ = 'Jeffrey Slort'

from flask import Blueprint, render_template,request
from flask.ext.mail import Message
from app import mailer

websiteBP = Blueprint("website",__name__,template_folder="templates")

@websiteBP.route('/')
def index():
    return render_template("index.html", id="yomamma2")

@websiteBP.route("/mail/contact",methods=["POST"])
def mail():
    msg = Message(subject="Contactformulier website",
                  recipients=["mail@jeffreyslort.nl"],
                  body=request.form["message"],
                  sender=(request.form["name"],request.form["email"]))
    try:
        mailer.send(msg)
    except:
        return "Er is iets fout gegaan!"


    return "SEND"