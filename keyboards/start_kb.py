from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def start_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Погода")
    kb.button(text="Гороскоп")
    kb.button(text="Курс валют")
    kb.button(text="Перевод")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)