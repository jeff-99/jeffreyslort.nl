__author__ = 'Jeffrey Slort'

from flask_wtf import Form
from wtforms.fields.html5 import DateField
from wtforms.fields import SubmitField, HiddenField, StringField,TextAreaField,SelectField
from wtforms.validators import length, optional
import datetime

class BlogPostForm(Form):
    datum = DateField("datum",default=datetime.datetime.today())
    titel = StringField("Titel")
    submit = SubmitField("Opslaan")
    md = TextAreaField(id="text")
    html= HiddenField(id="hiddenhtml")
    categorie = StringField("Categorie :")
    excerpt = TextAreaField("Samenvatting", validators=[length(max=140,message="te lang ouwe")])
    pub = SelectField("Publiceren",choices=[('1',"Publiceren"),('0',"Niet publiceren")],validators=[optional()])

def formify_post(post):
    """
    Functie om een BlogPost om te vormen zodat WTForms hem kan vullen bij het laden van het edit scherm
    """
    post.setdefault("md", post.body.md)
    return post