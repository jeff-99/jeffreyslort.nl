
from flask import Blueprint,redirect,render_template,url_for,request, session,flash,g
from flask.ext.login import login_required,login_user
from flask.ext.login import login_user
from app.auth.authutils import get_user, check_hash, logout_user
from mongokit.paginator import Paginator
from app import db
import datetime
from app.admin.forms import BlogPostForm, formify_post

adminBP = Blueprint("admin",__name__,template_folder="templates",static_folder="static")


@adminBP.route("/")
@login_required
def index():
    return render_template("admin_index.html")

@adminBP.route("/blogs-overzicht")
@login_required
def blog_overzicht():
    cursor = db.Post.fetch({},{"body":0,"slug":0})
    return render_template("blog-overzicht.html", posts=list(cursor))

@adminBP.route("/blog-edit/<ObjectId:post_id>", methods=["GET","POST"])
@login_required
def blog_edit(post_id):
    post = db.Post.get_from_id(post_id)
    form = BlogPostForm(request.form,obj=formify_post(post))
    if form.validate_on_submit():

        post.titel = form.titel.data
        post.body.md = form.md.data
        post.body.html= form.html.data
        post.excerpt = form.excerpt.data
        post.datum = datetime.datetime.combine(form.datum.data,datetime.time.min)
        post.pub = bool(form.pub.data)
        post.last_updated = datetime.datetime.now()

        if hasattr(post,"md"): post.pop("md")
        post.save()
    else:
        for i in form.errors:
            flash(i)
    return render_template("blog-edit.html", post=post,form=form)

@adminBP.route("/blog-create")
@login_required
def create():
    post = db.Post()
    post.save()
    return redirect(url_for("admin.blog_edit",post_id=post._id))


@adminBP.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = get_user(request.form["user"])
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

@adminBP.route("/logout")
@login_required
def logout():
    logout_user()
    print session
    return redirect(url_for("website.index"))