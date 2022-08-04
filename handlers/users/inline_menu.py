from aiogram import types

from keyboards.inline import ikb_menu
from loader import dp

@dp.message_handler(text='inline_menu')
async def show_inline_menu(message: types.Message):
    await message.answer('Inline_buttons', reply_markup=ikb_menu)