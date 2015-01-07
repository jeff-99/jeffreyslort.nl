from flask.ext.mongokit import Document
from datetime import datetime

class Post(Document):
    __collection__= "posts"
    structure = {
        "titel": unicode,
        "body": unicode,
        "excerpt":unicode,
        "datum": datetime,

        "permalink": unicode,
        "slug":unicode,
    }
    required_fields = ["titel","excerpt","datum","body"]
    use_dot_notation = True
