from flask import Flask, request, jsonify, render_template, Response, abort
from flask_sqlalchemy import SQLAlchemy
from config import Config
from sqlalchemy import Column, Integer, String, Enum, DateTime
from datetime import datetime, timedelta
import enum, json

app = Flask(__name__)
app.config.from_object(Config)
rds = SQLAlchemy(app)
app.debug = True

from models import *



@app.cli.command('db_create')
def db_create():
    rds.create_all()
    print('Database created!')

@app.cli.command('db_drop')
def db_drop():
    rds.drop_all()
    print('Database dropped!')

@app.cli.command('db_seed')
def db_seed():
    tsk1 = Task(
                name='Cook Eggs',
                description='Cooking eggs for the family',
                priority=1,
                status='ACTIVE'
                )

    tsk2 = Task(
                name='Boil Water',
                description='Heating up water on the stove',
                priority=3,
                status='PENDING'
                )

    
    rds.session.add(tsk1)
    rds.session.add(tsk2)
    rds.session.commit()
    print('Database seeded')

@app.errorhandler(400)
def invalid_request(e):
    return jsonify(error=str(e)), 400

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(422)
def resource_unprocessable(e):
    return jsonify(error=str(e)), 422


@app.route("/task_create", methods=["POST"])
def task_create():

    try:
        description = request.form['description']
        name = request.form['name']
        priority = int(request.form['priority'])
        runtimeHours = int(request.form['runtimeHours'])
        runtimeMinutes = int(request.form['runtimeMinutes'])
        runtimeSeconds = int(request.form['runtimeSeconds'])
    except:
        abort(422, description="Invalid input detected")

    # Ensure name is valid
    name = name.strip()
    if (len(name) < 1):
        abort(422, description="name must be 1 or more alphanumeric characters")

    # Ensure priority is between 1 and 5
    if (priority < 1 or priority > 5):
        abort(422, description="priority (%d) must be betwen 1 - 5" % priority)

    # Ensure runtime hours are less than 24
    if runtimeHours > 23:
        abort(422, description="Hour (%d) must be less than 24" % runtimeHours)

    # Ensure runtime minutes are between 0 - 59
    if runtimeMinutes > 59:
        abort(422, description="Minute (%d) must be less than 60" % runtimeMinutes)

    # Ensure runtime seconds are between 0 - 59
    if runtimeSeconds > 59:
        abort(422, description="Second (%d) must be less than 60" % runtimeSeconds)

    # Ensure total time is more than 5 seconds long
    runtimeTotal = runtimeHours * 3600 + runtimeMinutes * 60 + runtimeSeconds
    if runtimeTotal < 6:
        abort(422, description="Total runtime (%d seconds) must be greater than 5 seconds" % runtimeTotal)

    currenttime = datetime.now()
    endtime = currenttime + timedelta(seconds=runtimeTotal)

    new_task = Task(
        name = name,
        description = description,
        priority = priority,
        starttime = currenttime,
        currenttime = currenttime,
        createdtime = currenttime,
        endtime = endtime
    )

    rds.session.add(new_task)
    rds.session.commit()

    return Response('{"message":"Task created"}', mimetype='application/json')

@app.route("/task/<int:taskId>", methods=["GET"])
def task(taskId):
    if request.method == 'GET':
        row = Task.query.filter(Task.task_id == taskId).one_or_none()
        
        if row is None:
            abort(404, description="Task not found")
        
        return Response(json.dumps(task2Dict(row), default = taskConverter), mimetype='application/json')


@app.route("/task_update/<int:taskId>", methods=["PUT"])
def task_update(taskId):
    if request.method == 'PUT':
        row = Task.query.filter(Task.task_id == taskId).one_or_none()
        if row is None:
            abort(404, description="Task not found")

        currenttime = datetime.now()
        row.currenttime = currenttime
        
        if request.json:
            status = request.json['status']
            
            # Verify that the provided status is valid
            status_valid = False
            for name, member in StatusEnum.__members__.items():
                if (name == status):
                    status_valid = True
            if status_valid:
                row.status = request.json['status']
            else:
                abort(422, description="Status (%s) not valid. Expecting: PENDING, ACTIVE or COMPLETED" % status)

        rds.session.commit()
        return jsonify(message='Task updated')
    else:
        abort(400, description="Invalid request method performed")


@app.route("/tasks", methods=["GET"])
def tasks():
    dic_arr = []
    for row in Task.query.all():
        taskitem = task2Dict(row)
        dic_arr.append(taskitem)

    return Response(json.dumps(dic_arr, default = taskConverter), mimetype='application/json')



@app.route('/')
def home():
    return  jsonify(message='No Path specified!'), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0')


def task2Dict(row):
    di = {
        "task_id": row.task_id,
        "name": row.name,
        "description": row.description,
        "priority": row.priority,
        "starttime": row.starttime,
        "endtime": row.endtime,
        "currenttime": row.currenttime,
        "createdtime": row.createdtime,
        "status": row.status
    }

    return di

def taskConverter(o):
    # datetime isn't serializable, so "toString" it
    if isinstance(o, datetime):
        return o.__str__()
    # enum isn't serializable, so return name
    if isinstance(o, StatusEnum):
        return o.name

