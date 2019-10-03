import threading, logging, time
from models import StatusEnum
from app import Task
from datetime import datetime, timedelta

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    # filename='taskthread.log', filemode='w',
                    ) 

class TaskThread(threading.Thread):

    sleeptime = 10 # seconds to sleep
    thread_state = 1 # 0: paused, 1: active, 2: sleeping
    currenttime = datetime.now()


    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, group=group, target=target, name=name)
        self.args = args
        self.kwargs = kwargs
        self.rds = kwargs['rds']
        return

    def pause(self):
        self.thread_state = 0
        self.sleeptime = 60

    def activate(self):
        self.thread_state = 1
        self.sleeptime = 10

    def run(self):
        while True:
            self.currenttime = datetime.now()

            # Check if processing is paused
            if self.thread_state < 1:
                logging.info('Thread going to sleep for {0} seconds'.format(self.sleeptime))
                time.sleep(self.sleeptime)
                continue

            # Get all PENDING or ACTIVE tasks, sorted by priority
            self.thread_state = 1
            task_list = Task.query.filter(Task.status != "COMPLETED").order_by(Task.priority).all()
            for row in task_list:
                logging.info('Found a %s task' % row.status.name)
                row_updated = 0

                #  Verify if ACTIVE or old tasks are COMPLETED
                if row.endtime < self.currenttime:
                    row.status = "COMPLETED"
                    row_updated = 1

                
                # Verify if PENDING tasks should be set to ACTIVE
                if row.status == StatusEnum.PENDING:
                    if row.starttime < self.currenttime:
                        row.starttime = self.currenttime
                        row.status = "ACTIVE"
                        row_updated = 1


                #update row in DB
                if row_updated == 1:
                    logging.info('Task ({0}) is being updated to {1}'.format(row.name, row.status))
                row.currenttime = self.currenttime
                self.rds.session.commit()
            
            logging.info('Thread going to sleep for {0} seconds'.format(self.sleeptime))
            self.thread_state = 2
            time.sleep(self.sleeptime)


    def fake_query(self):
        currenttime = datetime.now()
        endtime = currenttime + timedelta(seconds=600)

        tsk1 = {
                "name":'Cook Eggs',
                "description":'Cooking eggs for the family',
                "priority":1,
                "status":'PENDING',
                "starttime": currenttime,
                "currenttime": currenttime,
                "createdtime": currenttime,
                "endtime": endtime
                }

        tsk2 = {
                "name":'Talk',
                "description":'Talking to neighbors',
                "priority":4,
                "status":'ACTIVE',
                "starttime": currenttime,
                "currenttime": currenttime,
                "createdtime": currenttime,
                "endtime": endtime
                }

        dic_arr = []
        dic_arr.append(tsk1)
        dic_arr.append(tsk2)
        return dic_arr
    

if __name__ == '__main__':
    pass