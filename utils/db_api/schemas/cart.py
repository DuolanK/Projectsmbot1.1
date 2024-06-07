from utils.db_api.db_gino import TimedBaseModel
from sqlalchemy import Column, BigInteger, ForeignKey, sql

class CartItem(TimedBaseModel):
    __tablename__ = 'cart_items'
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.user_id'))
    item_id = Column(BigInteger, ForeignKey('menu.id'))

    query: sql.select