__author__ = 'Jeffrey Slort'

from app import db
from hashlib import sha1
from flask.ext.login import _get_user, user_logged_out, COOKIE_NAME
from flask import session,current_app,request

def get_user(username):
    user = db.User.find_one({"username":username})
    return user

def check_hash(user,passw):
    if user.passw == sha1(passw).hexdigest():
        return True
    else:
        return False

def logout_user():
    '''
    Logs a user out. (You do not need to pass the actual user.) This will
    also clean up the remember me cookie if it exists.

    Verwijderd sessie ook uit de database - kopie van Flask-Login logout_user
    '''

    user = _get_user()

    if 'user_id' in session:
        user_id = session.pop('user_id')
        # delete from db
        db.sessions.remove({"session.user_id":user_id})

    if '_fresh' in session:
        session.pop('_fresh')

    cookie_name = current_app.config.get('REMEMBER_COOKIE_NAME', COOKIE_NAME)
    if cookie_name in request.cookies:
        session['remember'] = 'clear'



    user_logged_out.send(current_app._get_current_object(), user=user)

    current_app.login_manager.reload_user()
    return True