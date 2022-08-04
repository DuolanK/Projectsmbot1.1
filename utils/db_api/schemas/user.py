from utils.db_api.db_gino import TimedBaseModel
from sqlalchemy import Column, BigInteger, String, sql

class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    name = Column(String(200))
    username = Column(String(50))
    status = Column(String(30))

    query: sql.select