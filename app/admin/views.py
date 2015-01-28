
from flask import Blueprint,redirect,render_template,url_for,request, g
from flask.ext.login import login_required,login_user


adminBP = Blueprint("admin",__name__,template_folder="templates")



@adminBP.route("/")
@login_required
def index():
    print g.user
    return "welkom in de admin , meneer {}".format(g.user.username)
