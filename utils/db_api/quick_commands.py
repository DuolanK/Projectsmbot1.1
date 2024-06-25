from asyncpg import UniqueViolationError
import logging
from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User
from utils.db_api.schemas.menu import MenuItem
from utils.db_api.schemas.cart import CartItem
async def add_user(user_id: int, username: str, status: str):
    try:
        user = User(user_id=user_id, username=username, status=status)
        await user.create()
    except UniqueViolationError:
        print('user was not added')

async def register_user(user_id: int, username: str, name: str, birth: str, sex: bool, geo: str, time: str):
    try:
        logging.info(f'Registering user with id {user_id}, username {username}, name {name}, birth {birth}, sex {sex}, geo {geo}, time {time}')
        new_user = User(
            user_id=user_id,
            username=username,
            name=name,
            birth=birth,
            sex=sex,
            geo=geo,
            time=time,
            status="active"  # или другой статус по умолчанию
        )
        await new_user.create()
    except UniqueViolationError:
        logging.error('User was not added: UniqueViolationError')
    except Exception as e:
        logging.error(f'User was not added: {e}')
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


async def select_menu():
    return await MenuItem.query.where(MenuItem.status == True).gino.all()

async def select_menu_item(item_id: int):
    return await MenuItem.query.where(MenuItem.id == item_id).gino.first()

async def add_menu_item(name: str, description: str, price: str, image: str, status: bool):
    new_item = MenuItem(name=name, description=description, price=price, image=image, status=status)
    await new_item.create()

async def delete_menu_item(item_id: int):
    item = await select_menu_item(item_id)
    if item:
        await item.delete()

# Новые функции для работы с корзиной
async def add_to_cart(user_id: int, item_id: int):
    new_cart_item = CartItem(user_id=user_id, item_id=item_id)
    await new_cart_item.create()

async def get_cart_items(user_id: int):
    return await CartItem.query.where(CartItem.user_id == user_id).gino.all()
