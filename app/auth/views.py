__author__ = 'Jeffrey Slort'

from flask import Blueprint, request,redirect, render_template, url_for,flash
from flask.ext.login import login_user
from app.auth.authutils import get_user, check_hash

authBP = Blueprint("auth",__name__,template_folder="templates")

@authBP.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = get_user(request.form["name"])
        if user is not None and check_hash(user,request.form["passw"]):
            login_user(user)
            if not request.args.get("next"):
                return redirect(url_for("admin.index"))
            else:
                return redirect(request.args.get("next"))
        else:
            flash("U gebruikersnaam of wachtwoord klopt niet")
            return render_template("login.html")
    else:
        return render_template("login.html")