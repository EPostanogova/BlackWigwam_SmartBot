import logging
import datetime

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('SmartBot')

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from stickers import stickers
from config import TOKEN
from src.cameraman import Cameraman
from database.database import Database

bot = Bot(token=TOKEN)#,proxy='http://10.128.0.90:8080')
dp = Dispatcher(bot)
photo = Cameraman()


from constants.settings import DB_DATA
DB=Database(db_path = DB_DATA)
DB.create_users_table()
DB.create_commands_table()

def add_info_to_db(message, commands, DB):
    info_dir = {'id': message.from_user.id,
                'user_id': message.from_user.id,
                'first_name': message.from_user.first_name,
                'last_name': message.from_user.last_name,
                'command': commands, 'time_stamp': datetime.datetime.now()}
    DB.add_new_user(user_info=info_dir)
    DB.add_command(info=info_dir)
    DB.get_all_records(table_name='Users')
    DB.get_all_records(table_name='Cmd_table')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("С моей помощью Вы можете получить доступ к объекту под кодовым именем Wigwam")
    commands='start'
    add_info_to_db(message, commands, DB)





@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("start - краткая информация о боте \n" \
                        " help - список команд с описанием \n" \
                        "photo - получить мнгновенную фотографию вигвама \n")
    commands = 'help'
    add_info_to_db(message, commands, DB)

@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):
    try:
        photo.get_image()
    except ValueError as err:
        await bot.send_message(message.from_user.id, f"Изображение пустое, пожалуйста, проверьте подключение камеры. {err}")
        return
    commands = 'photo'
    add_info_to_db(message, commands, DB)

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
async def sticker(message: types.Message):
    print(message.sticker)
    await message.reply("Крутой стикер!")
    await bot.send_sticker(message.chat.id, sticker=stickers["Like"])


if __name__ == '__main__':
    executor.start_polling(dp)