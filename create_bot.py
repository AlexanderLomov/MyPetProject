from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN

storage = MemoryStorage()

TOKEN_API = TOKEN

bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=storage)