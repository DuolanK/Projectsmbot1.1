from aiogram import types
from aiogram.dispatcher import FSMContext

from filters import IsPrivate
from loader import dp
from aiogram.dispatcher.filters import Command
from utils.db_api import quick_commands

from states import register

@dp.message_handler(IsPrivate(), Command('register'))
async def register_(message: types.Message):
    await message.answer('Привет, введи своё ФИО')
    await register.test1.set()


@dp.message_handler(state=register.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test1=answer)
    await message.answer('введи дату рождения')
    await register.test2.set()
@dp.message_handler(state=register.test2)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test2=answer)
    await message.answer('укажи свой пол')
    await register.test3.set()

@dp.message_handler(state=register.test3)
async def state3(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test3=answer)
    await message.answer('укажи где ты находишься')
    await register.test4.set()

@dp.message_handler(state=register.test4)
async def state4(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test4=answer)
    await message.answer('введи текущее время')
    await register.test5.set()


@dp.message_handler(state=register.test5)
async def state2(message:types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(test5=answer)
    name = await state.get_data('test1')
    birth = await state.get_data('test2')
    sex = await state.get_data('test3')
    geo = await state.get_data('test4')
    time = await state.get_data('test5')
    await message.answer(f'registration complete'
                         f'your name {name}{birth}{sex}{geo}{time}\n')
    await state.finish()
    await quick_commands.register_user(user_id=message.from_user.id, name=name, birth=birth, sex=sex, geo=geo)