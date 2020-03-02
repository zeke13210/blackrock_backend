import os

class Config(object):
    # if 'RDS_HOSTName' in os.environ:    # Production
        # dbName = os.environ['RDS_DB_NAME']
        # user = os.environ['RDS_USERNAME']
        # password = os.environ['RDS_PASSWORD']
        # hostName = os.environ['RDS_HOSTNAME']
        # port = os.environ['RDS_PORT']
    dbName = "TaskManagerDB"
    user = "postgres"
    password = "tocTaskManager"
    hostName = "blackrockdbinstance.c0uikdugnayd.us-east-1.rds.amazonaws.com"
    port = "5432"
    postURL = "postgresql://" + user + ":" + password + "@" + hostName + ":" + port + "/" + dbName
    SQLALCHEMY_DATABASE_URI = postURL
    #else:       # Dev
        #SQLALCHEMY_DATABASE_URI = os.environ.get('POST_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
