from aiogram import types
from loader import dp
import requests
from openai import OpenAI


from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import OPENAI_API_KEY

from aiogram.dispatcher.filters import Text

client = OpenAI(api_key=OPENAI_API_KEY)
storage = MemoryStorage()

# Функция для генерации ответа с помощью OpenAI API
def generate_response_from_openai(prompt):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=150)
    generated_text = response.choices[0].message.content.strip()
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
                         f'You are subscribed')

@dp.message_handler(text='unsubscribe')
async def buttons(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'You are unsubscribed')

def generate_response_locally(input_text):
    url = 'http://localhost:8501'
    data = {'input_text': input_text}
    response = requests.post(url, json=data)
    generated_text = response.json().generated_text
    return generated_text