import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger ('SmartBot')

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("С моей помощью Вы можете получить доступ к объекту под кодовым именем Wigwam")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("start - краткая информация о боте \n help - список команд с описанием")


@dp.message_handler()
async def hello_response(msg: types.Message):
    if 'привет' in msg.text.lower():
        await bot.send_message(msg.from_user.id, f"Здравствуй,{msg.from_user.first_name}!")
    elif 'пока' in msg.text.lower():
        await bot.send_message(msg.from_user.id, f"Прощай,{msg.from_user.first_name}!")
    elif 'до свидания' in msg.text.lower():
        await bot.send_message(msg.from_user.id, f"До новых встречь,{msg.from_user.first_name}!")

@dp.message_handler(content_types=["sticker"])
async def sticker (message: types.Message):
    await message.reply("Крутой стикер! Я скоро тоже смогу их отправлять!")

if __name__ == '__main__':
    executor.start_polling(dp)
