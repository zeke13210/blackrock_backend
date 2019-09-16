from app import rds

class Task(rds.Model):
    __tablename__ = 'tasks'

    task_id = rds.Column(rds.Integer, primary_key=True)
    name = rds.Column(rds.String(64), index=True)
    description = rds.Column(rds.String(64))
    priority = rds.Column(rds.Integer)
    time = rds.Column(rds.String(64))
    starttime = rds.Column(rds.String(64))
    endtime = rds.Column(rds.String(64))
    createdtime = rds.Column(rds.String(64))
    status = rds.Column(rds.String(64))

    def __repr__(self):
        return '<User {}>'.format(self.name)