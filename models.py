from app import rds
from sqlalchemy import Column, Integer, String, Enum, DateTime
from datetime import datetime
import enum, os

db_table = os.environ.get('DB_TABLE','tasks')

class StatusEnum(enum.Enum):
    PENDING = 1
    ACTIVE = 2
    COMPLETED = 3

class Task(rds.Model):
    __tablename__ = db_table

    task_id     = Column(Integer, primary_key=True)
    name        = Column(String(64), index=True)
    description = Column(String(200))
    priority    = Column(Integer)
    starttime   = Column(DateTime)
    endtime     = Column(DateTime)
    currenttime = Column(DateTime)
    createdtime = Column(DateTime)
    status      = Column(Enum(StatusEnum), default=StatusEnum.PENDING)

    def __repr__(self):
        return '{}'.format(self.name)

