from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(user_id: int, full_name: str, username: str, status: str):
    try:
        user = User(user_id=user_id, full_name=full_name, username=username, status=status)
        await user.create()
    except UniqueViolationError:
        print('user was not added')


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def count_users():
    count = db.func.count(User.user_id).gino.scalar()
    return count

async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user

async def update_status(user_id, status):
    user = await select_user(user_id)
    await user.update(status=status).apply()