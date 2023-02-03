from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="6052931568:AAE_6CjKCrpS7LNna-HIN4KhG3ix2eCIBHU")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def a(message):
    await message.reply("asd")


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напине что-нибст тебе в ответ!")


if __name__ == '__main__':
    print("Starting")
