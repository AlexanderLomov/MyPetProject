from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Synonyms')
b2 = KeyboardButton('/English_Tenses')
b3 = KeyboardButton('/Vocabulary')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2, b3)