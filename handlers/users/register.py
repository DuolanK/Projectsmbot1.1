from aiogram import types
from aiogram.dispatcher import FSMContext

from filters import IsPrivate
from loader import dp
from aiogram.dispatcher.filters import Command


from states import register

@dp.message_handler(IsPrivate(), Command('register'))
async def register_(message: types.Message):
    await message.answer('Hi input your name')
    await register.test1.set()

@dp.message_handler(state=register.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test1=answer)
    await message.answer('input your table')
    await register.test2.set()

@dp.message_handler(state=register.test2)
async def state2(message:types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test2=answer)
    name = await state.get_data('test1')
    table = await state.get_data('test2')
    await message.answer(f'registration complete'
                         f'your name {name}\n'
                         f'your table {table}\n')