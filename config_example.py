import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = "enter aws postgres url here"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
