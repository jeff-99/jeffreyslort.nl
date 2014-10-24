__author__ = 'Jeffrey Slort'

from flask.ext.mongokit import Document
from datetime import datetime

class Blog(Document):
    __collection__ = "blogs"
    structure = {
        "titel": unicode,
        "body": unicode,
        "tags": list,
        "timestamp" : datetime
    }
    required_fields = ["titel","body","timestamp"]
    use_dot_notation = True

class Sectie(Document):
    __collection__ = "secties"
    structure = {
        "jan": unicode
    }

def pimpie():
    return "jaaaaa"