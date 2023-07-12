from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

@dp.message_handler(commands=["start", "help"])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'What do you want to do?', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Send a PM to the Bot, please.')

@dp.message_handler(commands=['English_Tenses'])
async def pizza_menu_command(message : types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_menu_command, commands=['English_Tenses'])
