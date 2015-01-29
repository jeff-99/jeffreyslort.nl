import os

MONGODB_DATABASE = "jeffreyslort"
MONGODB_HOST = "localhost"
MONGODB_PORT = 27017

MAIL_SERVER = "mail.jeffreyslort.nl"
MAIL_PORT = 587
MAIL_USERNAME = "mail@jeffreyslort.nl"
MAIL_PASSWORD = "poiuyt09"
MAIL_USE_SSL = False

SECRET_KEY = os.urandom(1024)
WTF_CSRF_ENABLED = True