__author__ = 'Jeffrey Slort'

from flask import Blueprint, redirect, url_for, render_template, request
from mongokit.paginator import Paginator
from app import db

blogBP = Blueprint("blog",__name__, template_folder="templates")

@blogBP.route("/")
def index():
    return redirect(url_for("blog.overzicht"))

@blogBP.route("/overzicht", defaults={"pagina": 1})
@blogBP.route("/overzicht/<int:pagina>")
def overzicht(pagina):
    cat = request.args.get("cat")
    search = request.args.get("zoeken")
    query = request.query_string
    print query
    next_page = None
    previous_page = None

    if not cat and not search:
        cursor = db.Post.fetch()
    elif cat and not search:
        cursor = db.Post.fetch({"categorie":cat})
    elif search and not cat:
        cursor = db.Post.fetch({ "$text": { "$search": search, "$language": "nl" } })
    else:
        cursor = db.Post.fetch({"categorie":cat, "$text": { "$search": search, "$language": "nl" } })

    p = Paginator(cursor=cursor,page=pagina,limit=3)

    if p.has_next:
        next_page = p.next_page
    if p.has_previous:
        previous_page = p.previous_page

    return render_template("blog_overzicht.html", posts=p.items,next=next_page,prev=previous_page,query=query)


@blogBP.route("/<int:jaar>/<string:titel>")
def post(jaar,titel):
    post = db.Post.find_one_or_404({"titel":titel})
    return render_template("post.html",post=post)


@blogBP.route("/permalink/<string:hash>")
def perma(hash):
    return "permalinks"