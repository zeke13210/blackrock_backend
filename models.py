from sqlalchemy import Column, Integer, String, Enum, DateTime
from datetime import datetime
import enum, os
db_table = os.environ.get('DB_TABLE','tasks')

class StatusEnum(enum.Enum):
    PENDING = 1
    ACTIVE = 2
    COMPLETED = 3