from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def weather_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Великий Новгород")
    kb.button(text="Архангельск")
    kb.button(text="Санкт-Петербург")
    kb.button(text="Москва")
    kb.button(text="Главное меню")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)