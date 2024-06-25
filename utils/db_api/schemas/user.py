from utils.db_api.db_gino import TimedBaseModel
from sqlalchemy import Column, BigInteger, String, sql, Boolean, Time, Integer, Date

class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    name = Column(String(200))
    username = Column(String(50))
    birth = Column(String(50))
    sex = Column(Boolean)
    geo = Column(String(50))
    time = Column(String(50))
    status = Column(String(30))
    refer_score = Column(Integer)

    query: sql.select