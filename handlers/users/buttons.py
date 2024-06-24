from aiogram import types
from loader import dp
import requests


@dp.message_handler(text='10')
async def buttons(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f' 10')
@dp.message_handler(text='subscribe')
async def buttons(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f' Youre subscibed')

@dp.message_handler(text='unsubscribe')
async def buttons(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f' Youre unsubscibed')




def generate_response_locally(input_text):
    print('чтото живо')
    url = 'http://localhost:8501'  # Замените на адрес вашего локального сервера
    data = {'input_text': input_text}
    response = requests.post(url, json=data)
    generated_text = response.json().get('generated_text')
    return generated_text
