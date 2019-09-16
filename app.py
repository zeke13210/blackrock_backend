from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
rds = SQLAlchemy(app)
app.debug = True
migrate = Migrate(app, rds)

from models import *

@app.route('/', methods=['GET', 'POST'])
def task():
    if request.method == 'GET':
        return ('Hey, we have Flask in a Docker container!!!!')
    elif request.method == 'POST'
        # task = Task(task_id="123", name="The is the first task")
        # rds.session.add(task)
        # rds.session.commit()
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')
