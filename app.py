from flask import Flask, request, jsonify, render_template, Response, abort
from flask_sqlalchemy import SQLAlchemy
from config import Config
from sqlalchemy import Column, Integer, String, Enum, DateTime
from datetime import datetime, timedelta
import enum, json, os, sys


app = Flask(__name__)
app.config.from_object(Config) #add config of AWS postgres db
rds = SQLAlchemy(app) #initialize app with sql alchemy
app.debug = True

from models import *
import cli
from taskthread import TaskThread


# Convert a task sqlalchemy database row to a dict, 
# so that it can be converted to JSON. Used by Flask.Response()
def task2Dict(row):
    #takes row and converts to json obj and returns the obj
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


# Define how to serialize elements that are not normally serializeable,
# so that they can be converted to JSON. Used by Flask.Response()
def taskConverter(o):
    # datetime isn't serializable, so "toString" it
    #if input is datetime obj return string of obj
    if isinstance(o, datetime):
        return o.__str__()
    # enum isn't serializable, so return name
    if isinstance(o, StatusEnum):
        return o.name


@app.cli.command('db_create')
def db_create():
    """
    Execute with cmd: "flask db_create" to create
    all tables
    """
    rds.create_all()
    print('Database created!')

@app.cli.command('db_drop')
def db_drop():
    """
    Execute with cmd: "flask db_drop" to remove tables

    """
    rds.drop_all()
    print('Database dropped!')

@app.cli.command('db_showtable')
def db_showtable():
    print(Task.__tablename__)

@app.cli.command('db_seed')
def db_seed():

    """
    When executed with flask cmd will create test data
    based on tsk1 & tsk2

    """
    tsk1 = Task(
                name='Cook Eggs',
                description='Cooking eggs for the family',
                priority=1,
                status='ACTIVE',
                starttime = currenttime,
                currenttime = currenttime,
                createdtime = currenttime,
                endtime = endtime
                )

    tsk2 = Task(
                name='Boil Water',
                description='Heating up water on the stove',
                priority=3,
                status='PENDING',
                starttime = currenttime,
                currenttime = currenttime,
                createdtime = currenttime,
                endtime = endtime
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


# API: Route to Create a task 
@app.route("/task_create", methods=["POST"])
def task_create():
    """
    recieves HTML form and mapps the below fields then validates form fields
    using certain conditions

    description, name, priority, run time hours, run time minutes and run time seconds

    """
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
    new_task_id = new_task.task_id

    str = '{"message":"Task created", "task_id":%d}' % new_task_id
    return Response(str, mimetype='application/json')


# API: Route to get the task data for the specified taskId
@app.route("/task/<int:taskId>", methods=["GET"])
def task(taskId):
    """
    function returns JSOn of task when API hits /task/ task ID
    if no id found then returns error msg task not found
    """
    if request.method == 'GET':
        row = Task.query.filter(Task.task_id == taskId).one_or_none()
        
        if row is None:
            abort(404, description="Task not found")
        
        return Response(json.dumps(task2Dict(row), default = taskConverter), mimetype='application/json')


# API: Route to update the task data for the specified taskId
@app.route("/task_update/<int:taskId>", methods=["PUT"])
def task_update(taskId):
    """
    function updates task when api gives task ID. replaces old time with
    current time of when API is called
    """
 
    row = Task.query.filter(Task.task_id == taskId).one_or_none()
    if row is None:
        abort(404, description="Task not found")

        currenttime = datetime.now()
        row.currenttime = currenttime
        
        if request.json:
            status = request.json['status']
            
            # Verify that the provided status is valid
            if status in StatusEnum.__members__.keys():
                row.status = status
            else:
                abort(422, description="Status (%s) not valid. Expecting: PENDING, ACTIVE or COMPLETED" % status)

        rds.session.commit()
        return jsonify(message='Task updated')
    else:
        abort(400, description="Invalid request method performed")


# API: Route to get All tasks
@app.route("/tasks", methods=["GET"])
def tasks():

    task_query = Task.query
    if 'status' in request.args:
        status = request.args.get('status')
        stat_list = status.split(',')
        
        # Ensure status is valid
        for stat in stat_list:
            if stat not in StatusEnum.__members__.keys():
                abort(422, description="Status (%s) not valid. Expecting a comma separated combination of: PENDING, ACTIVE, COMPLETED (or no query, for all tasks)" % stat)
                print(stat)
        
        # Set status filter
        task_query = task_query.filter(Task.status.in_(stat_list))
        

    dic_arr = []
    for row in task_query.all():
        taskitem = task2Dict(row)
        dic_arr.append(taskitem)

    return Response(json.dumps(dic_arr, default = taskConverter), mimetype='application/json')


@app.route('/')
def home():
    return  jsonify(message='No Path specified!'), 400


# ADMIN: Enable the task thread to poll the database
@app.route("/admin/thread_start", methods=["GET"])
def thread_sart():
    if t.thread_state > 0:
        return jsonify(message='Thread already ACTIVE')

    t.activate()
    return jsonify(message='Thread REACTIVATED: May take up to 60 secs to restart')


# ADMIN: Stop the task thread from polling the database
@app.route("/admin/thread_pause", methods=["GET"])
def thread_pause():
    t.pause()
    return jsonify(status = 'PAUSED')


# ADMIN: Get a status on the task thread
@app.route("/admin/thread_status", methods=["GET"])
def thread_status():

    if t.thread_state == 0:
        currenttime = datetime.now()
        sleep_time = round(t.sleeptime - (currenttime - t.currenttime).total_seconds())
        di = {'status':'PAUSED', 'message':'Resting for {0} secs'.format(sleep_time)}
        return jsonify(di)

    if t.thread_state == 1:
        di = {'status':'ACTIVE', 'message':'Actively processing'}
        return jsonify(di)

    if t.thread_state == 2:
        currenttime = datetime.now()
        sleep_time = round(t.sleeptime - (currenttime - t.currenttime).total_seconds())
        di = {'status':'ACTIVE', 'message':'Resting for {0} secs'.format(sleep_time)}
        return jsonify(di)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

# Do not start the task thread if a command line method is executed
if not (len(sys.argv) > 1 and sys.argv[1] in app.cli.commands):
    t = TaskThread(name='TaskmanThread',kwargs={'rds':rds})
    t.setDaemon(True)
    t.start()
