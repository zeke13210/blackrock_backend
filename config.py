import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://<username>:<password>@<host>:<port>/<dbname>"
    SQLALCHEMY_TRACK_MODIFICATIONS = False