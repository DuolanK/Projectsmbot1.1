from aiogram import types
from loader import dp
from filters import  IsPrivate
from utils.misc import rate_limit
from utils.db_api import quick_commands

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from utils.db_api.schemas.menu import MenuItem
from utils.db_api.schemas.cart import CartItem

# Команда для старта
# @rate_limit(limit=3)
# @dp.message_handler(IsPrivate(), commands=['start'])
# async def command_start(message: types.Message):
#     try:
#         user = await quick_commands.select_user(message.from_user.id)
#         if user.status == 'active':
#             await message.answer(f'Hi {message.from_user.full_name}\n')
#         elif user.status == 'banned':
#             await message.answer('You are banned')
#     except Exception:
#         await quick_commands.add_user(user_id=message.from_user.id,
#                                       username=message.from_user.username,
#                                       status='active')
#         await message.answer('Привет')


# Команда для бана // добавить проверку на админство!!!!!!!!!!!!
@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), commands=['ban'])
async def get_ban(message: types.Message):
    # await quick_commands.update_status('banned')
    await message.answer('User is banned', reply_markup=del_kb)

# Команда для разбанивания
@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), commands=['unban'])
async def get_unban(message: types.Message):
    await quick_commands.update_status('active')
    await message.answer('User is unbanned')

del_kb = types.ReplyKeyboardRemove()