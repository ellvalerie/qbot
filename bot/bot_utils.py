import os
from aiogram.types import Message
from aiogram.filters import CommandStart
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher


load_dotenv(find_dotenv())
bot = Bot(os.getenv('TOKEN'), parse_mode='HTML')
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет! <b>{message.from_user.first_name}</b>")