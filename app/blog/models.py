from flask.ext.mongokit import Document
from datetime import datetime

class Post(Document):
    __collection__="posts"
    structure = {
        "titel": unicode,
        "body": unicode,
        "samenvatting":unicode,
        "datum": datetime,

        "permalink": unicode,
        "slug":unicode,



    }
    use_dot_notation = True
