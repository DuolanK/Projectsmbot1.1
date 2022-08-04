from aiogram import types
from loader import dp

@dp.message_handler(text='subscribe')
async def buttons(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f' Youre subscibed (no)')

@dp.message_handler(text='unsubscribe')
async def buttons(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f' Youre unsubscibed (no)')