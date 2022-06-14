from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def horoscope_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    zodiak_sings = ["Овен", "Телец", "Близницы", "Рак", "Лев", "Дева",
         "Весы", "Скорпион", "Стрелец", "Козерог", "Водолей", "Рыбы"]
    for i in zodiak_sings:
        kb.button(text=i)
    kb.button(text="Главное меню")
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True)

