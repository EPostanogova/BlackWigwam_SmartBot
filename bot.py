import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger ('SmartBot')

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from stickers import stickers
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
     await message.reply("С моей помощью Вы можете получить доступ к объекту под кодовым именем Wigwam")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("start - краткая информация о боте \n"\
                        " help - список команд с описанием \n"\
                        "photo - получить мнгновенную фотографию вигвама \n")
@dp.message_handler()
async def hello_response(msg: types.Message):
    if 'привет' in msg.text.lower():
         await bot.send_message(msg.from_user.id, f"Здравствуй, {msg.from_user.first_name}!")
         await bot.send_sticker(msg.chat.id, sticker=stickers["Puppy"])
    elif 'пока' in msg.text.lower():
         await bot.send_message(msg.from_user.id, f"Прощай, {msg.from_user.first_name}!")
         await bot.send_sticker(msg.chat.id, sticker=stickers["Sad"])
    elif 'до свидания' in msg.text.lower():
         await bot.send_message(msg.from_user.id, f"До новых встреч, {msg.from_user.first_name}!")
         await bot.send_sticker(msg.chat.id, sticker=stickers["LoveBye"])

@dp.message_handler(content_types=["sticker"])
async def sticker (message: types.Message):
    print(message.sticker)
    await message.reply("Крутой стикер!")
    await bot.send_sticker(message.chat.id, sticker=stickers["Like"])



    
if __name__ == '__main__':
    executor.start_polling(dp)
