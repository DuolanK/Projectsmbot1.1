from utils.db_api.db_gino import TimeBaseModel
from sqlalchemy import Column, BigInteger, String, sql

class User(TimeBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    name = Column(String(200), primary_key=True)
    update_name = Column(String(50), primary_key=True)

    query: sql.select