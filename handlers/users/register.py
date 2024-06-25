from aiogram import types
from aiogram.dispatcher import FSMContext
import logging
from filters import IsPrivate
from loader import dp
from aiogram.dispatcher.filters import Command
from utils.db_api import quick_commands
from states import register


logging.basicConfig(level=logging.INFO)

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
async def state5(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(test5=answer)

    data = await state.get_data()
    name = data['test1']
    birth = data['test2']
    sex = data['test3']
    geo = data['test4']
    time = data['test5']

    logging.info(f'Collected data: {data}')

    # Преобразование пола в Boolean (True - мужчина, False - женщина)
    sex_bool = True if sex.lower() in ['м', 'мужчина', 'male'] else False

    # Добавление пользователя в базу данных
    await quick_commands.register_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        name=name,
        birth=birth,
        sex=sex_bool,
        geo=geo,
        time=time
    )

    await message.answer(f'Registration complete. Your data:\n'
                         f'Name: {name}\n'
                         f'Birth Date: {birth}\n'
                         f'Sex: {"Male" if sex_bool else "Female"}\n'
                         f'Location: {geo}\n'
                         f'Time: {time}')
    await state.finish()
