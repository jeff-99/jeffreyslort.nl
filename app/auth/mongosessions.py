__author__ = 'Jeffrey Slort'

from flask.sessions import SessionMixin, SessionInterface
from werkzeug.datastructures import CallbackDict
from uuid import uuid4
from datetime import datetime,timedelta
from itsdangerous import URLSafeSerializer, BadSignature

class MongoSession(CallbackDict, SessionMixin):

    def __init__(self, initial=None, sid=None):
        def on_update(self):
            self.modified = True
        CallbackDict.__init__(self, initial,on_update)
        self.sid = sid
        self.modified = False

class MongoSessionInterface(SessionInterface):

    def __init__(self, db_connection=None):
        self.salt = "salty"
        if db_connection is not None:
            self.db = db_connection

    def get_serializer(self, app):
        if not app.secret_key:
            return None
        return URLSafeSerializer(app.secret_key,
                                      salt=self.salt)


    def generate_sid(self):
        return str(uuid4())

    def open_session(self, app, request):
        s = self.get_serializer(app)
        if s is None:
            return None
        val = request.cookies.get(app.session_cookie_name)
        if val:
            try:
                sid = s.loads(val)
            except BadSignature:
                return MongoSession(sid=self.generate_sid())

            stored_session = self.db.sessions.find_one({"_id":sid})
            if stored_session:
                if stored_session.get("expiration") > datetime.utcnow():
                    return MongoSession(initial=stored_session["session"],sid=sid)

        return MongoSession(sid=self.generate_sid())

    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)
        if not session:
            response.delete_cookie(app.session_cookie_name, domain=domain)
            return
        if self.get_expiration_time(app, session):
            expiration = self.get_expiration_time(app, session)
        else:
            expiration = datetime.utcnow() + timedelta(days=1)

        if session.has_key("user_id"):
            sid = session.sid
            val = self.get_serializer(app).dumps(sid)

            self.db.sessions.update({'_id': sid},
                              {"$set": {
                               'session': session,
                               'expiration': expiration}}, True)

            response.set_cookie(app.session_cookie_name, val,
                                expires=self.get_expiration_time(app, session),
                                httponly=True, domain=domain)