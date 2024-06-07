from utils.db_api.db_gino import TimedBaseModel
from sqlalchemy import Column, BigInteger, String, sql, Boolean

class MenuItem(TimedBaseModel):
    __tablename__ = 'menu'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(200))
    description = Column(String(50))
    price = Column(String(30))
    image = Column(String(30))
    status = Column(Boolean, default=True)

    query: sql.select
