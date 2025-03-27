import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = '8147896283:AAEGR-yd3ThbIF6qu2k8PY4E4QNrOn-XvXI'

FLASK_URL = 'http://your-ngrok-url.ngrok.io/get_score'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Нажми /score, чтобы узнать текущий счет в игре.")

@dp.message_handler(commands=['score'])
async def get_score(message: types.Message):
    try:
        response = requests.get(FLASK_URL)
        data = response.json()
        click_count = data.get('click_count', 0)
        await message.reply(f"Текущий счет в игре: {click_count}")
    except Exception as e:
        await message.reply("Произошла ошибка при получении счета.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
