__author__ = 'Jeffrey Slort'

from flask.sessions import SessionMixin, SessionInterface
from werkzeug.datastructures import CallbackDict
from uuid import uuid4
from datetime import datetime,timedelta

class MongoSession(CallbackDict, SessionMixin):

    def __init__(self, initial=None, sid=None):
        def on_update(self):
            self.modified = True
        CallbackDict.__init__(self, initial,on_update)
        self.sid = sid
        self.modified = False

class MongoSessionInterface(SessionInterface):

    def __init__(self, db_connection=None):
        if db_connection is not None:
            self.db = db_connection

    def generate_sid(self):
        return str(uuid4())

    def open_session(self, app, request):
        sid = request.cookies.get(app.session_cookie_name)
        if sid:
            #: load session from database
            stored_session = self.db.sessions.find_one({"_id":sid})
            if stored_session:
                if stored_session.get("expiration") > datetime.utcnow():
                    return MongoSession(initial=stored_session,sid=sid)
        new_sid = self.generate_sid()
        return MongoSession(sid=new_sid)

    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)
        if not session:
            response.delete_cookie(app.session_cookie_name, domain=domain)
            return
        if self.get_expiration_time(app, session):
            expiration = self.get_expiration_time(app, session)
        else:
            expiration = datetime.utcnow() + timedelta(minutes=1)
        self.db.sessions.update({'_id': session.sid},
                          {'_id': session.sid,
                           'user_id': session["user_id"],
                           'expiration': expiration}, True)
        response.set_cookie(app.session_cookie_name, session.sid,
                            expires=self.get_expiration_time(app, session),
                            httponly=True, domain=domain)