import os

class Config(object):
    if 'RDS_HOSTName' in os.environ:    # Production
        dbName = os.environ['RDS_DB_NAME']
        user = os.environ['RDS_USERNAME']
        password = os.environ['RDS_PASSWORD']
        host = os.environ['RDS_HOSTNAME']
        port = os.environ['RDS_PORT']
        postURL = "postgresql://" + user + ":" + password + "@" + host + ":" + port + "/" + dbName
        SQLALCHEMY_DATABASE_URI = postURL
    else:       # Dev
        SQLALCHEMY_DATABASE_URI = os.environ.get('POST_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
