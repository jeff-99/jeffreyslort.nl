__author__ = 'Jeffrey Slort'

from app import db
from hashlib import sha1

def get_user(username):
    user = db.User.find_one({"username":username})
    return user

def check_hash(user,passw):
    if user.passw == sha1(passw).hexdigest():
        return True
    else:
        return False