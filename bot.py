import logging
import datetime
import aioschedule
import asyncio

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('SmartBot')

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from stickers import stickers
from config import TOKEN
from src.cameraman import Cameraman
from database.database import Database
from src.arduino import ArduinoConnector

bot = Bot(token=TOKEN)#,proxy='http://10.128.0.90:8080')
dp = Dispatcher(bot)
photo = Cameraman()
AC = ArduinoConnector(com_port='COM8', baudrate=115200)

global CHAT_ID
CHAT_ID = None

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
    #DB.drop_table(table_name='Users')



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("С моей помощью Вы можете получить доступ к объекту под кодовым именем Wigwam")
    commands='start'
    add_info_to_db(message, commands, DB)
    global CHAT_ID
    CHAT_ID = message.chat.id






@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("start - краткая информация о боте \n" \
                        " help - список команд с описанием \n" \
                        " temperature - показания термометра \n" \
                        " humidity - показания гигрометра \n" \
                        "photo - получить мгновенную фотографию вигвама \n")
    commands = 'help'
    add_info_to_db(message, commands, DB)

@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):
    try:
        dir=photo.get_image()
        with open(f'{dir}', "rb") as file:
            data = file.read()
        await bot.send_photo(message.from_user.id, photo=data)
    except ValueError as err:
        await bot.send_message(message.from_user.id, f"Изображение пустое, пожалуйста, проверьте подключение камеры. {err}")
        return
    commands = 'photo'
    add_info_to_db(message, commands, DB)

@dp.message_handler(commands=['temperature'])
async def process_temperature_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, f"Температура в Вигваме {AC.get_temperature(msg='t')} *C.")
    except BufferError as err:
        await bot.send_message(message.from_user.id, f"Невозможно получить данные. {err}")
        return
    commands = 'temperature'
    add_info_to_db(message, commands, DB)

@dp.message_handler(commands=['humidity'])
async def process_humidity_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, f"Влажность в Вигваме {AC.get_humidity(msg='h')} %.")
    except ValueError as err:
        await bot.send_message(message.from_user.id, f"Невозможно получить данные. {err}")
        return
    commands = 'humidity'
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

async def spammer():
    global CHAT_ID
    if CHAT_ID is not None:
     await bot.send_message(chat_id=CHAT_ID, text=AC.detector(msg='c'))

async def scheduler():
   aioschedule.every(30).seconds.do(spammer)
   while True:
       await aioschedule.run_pending()
       await asyncio.sleep(1)


async def on_startup(_):
  asyncio.create_task(scheduler())


@dp.message_handler(content_types=["sticker"])
async def sticker(message: types.Message):
    print(message.sticker)
    await message.reply("Крутой стикер!")
    await bot.send_sticker(message.chat.id, sticker=stickers["Like"])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)