__author__ = 'Jeffrey Slort'

from flask.ext.mongokit import Document

class User(Document):
    __collection__= "users"
    structure = {
        "username": unicode,
        "passw": unicode,
        "email":unicode,
        "name": unicode,
        "avatar": unicode
    }
    required_fields = ["username","passw"]
    use_dot_notation = True

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self._id

