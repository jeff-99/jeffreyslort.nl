__author__ = 'Jeffrey Slort'

from flask import Blueprint, render_template,request,g
from flask.ext.mail import Message
from app import mailer, db

websiteBP = Blueprint("website",__name__,template_folder="templates")

@websiteBP.route('/')
def index():
    return render_template("index.html", id="yomamma2")

@websiteBP.route("/<string:sectie>")
def sectie(sectie):
    doc = db.Sectie.fetch_one({"sectie":sectie},{"_id":0})
    if doc:
        if doc.get("type") == "overzicht":
            posts = [p for p in db.posts.find({"sectie":sectie})]
            return render_template(doc["template"],posts=posts)
        else:
            return render_template(doc["template"])
    else:
        return "Pagina bestaat nog niet!"

@websiteBP.route("/mail/contact",methods=["POST"])
def mail():
    msg = Message(subject="Contactformulier website",
                  recipients=["mail@jeffreyslort.nl"],
                  body=request.form["message"],
                  sender=(request.form["name"],request.form["email"]))
    try:
        mailer.send(msg)
        return "SEND"
    except:
        return "Er is iets fout gegaan!"
