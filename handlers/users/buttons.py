from aiogram import types
from loader import dp
import requests
import openai
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import OPENAI_API_KEY

from aiogram.dispatcher.filters import Text



openai.api_key = OPENAI_API_KEY
storage = MemoryStorage()




# Функция для генерации ответа с помощью OpenAI API
def generate_response_from_openai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    generated_text = response.choices[0].text.strip()
    return generated_text

# Обработчик для команды "Получить прогноз"
@dp.message_handler(Text(equals='Получить прогноз'))
async def get_forecast(message: types.Message):
    prompt = "Дай мне прогноз судьбы"
    response = generate_response_from_openai(prompt)
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'Лови свой прогноз!\n{response}')




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
