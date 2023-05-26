from aiogram import types
from loader import dp
from filters import  IsPrivate
from utils.misc import rate_limit
from utils.db_api import quick_commands


@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text='/start')
async def command_start(message: types.Message):
    try:
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'Hi {message.from_user.full_name}\n'
                                 f'Youre already registered')
        elif user.status == 'banned':
            await message.answer('Youre banned =D')
    except Exception:
        await quick_commands.add_user(user_id=message.from_user.id,
                                      username=message.from_user.username,
                                      status='active')
        await message.answer('youre registered')

@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text='/ban')
async def get_ban(message:types.Message):
    await quick_commands.update_status('ban')
    await message.answer('youre banned lol')

@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text='/unban')
async def get_ban(message:types.Message):
    await quick_commands.update_status('active')
    await message.answer('youre NOT banned lol')




