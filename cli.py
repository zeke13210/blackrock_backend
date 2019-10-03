from app import rds, app
from app import Task
from datetime import datetime, timedelta

@app.cli.command('db_create')
def db_create():
    rds.create_all()
    print('Database created!')

@app.cli.command('db_drop')
def db_drop():
    rds.drop_all()
    print('Database dropped!')

@app.cli.command('db_showtable')
def db_showtable():
    print(Task.__tablename__)

@app.cli.command('db_seed')
def db_seed():

    currenttime = datetime.now()
    endtime = currenttime + timedelta(seconds=600)

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
