from aiogram import Router
from aiogram.dispatcher.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.start_kb import start_kb

router = Router()  # [1]


@router.message(commands=["start"])  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "Проектируем",
        reply_markup=start_kb()
    )





@router.message(Text(text="Курс валют", text_ignore_case=True), state=None)
async def exchange_rate_cb(message: Message):
    await message.answer(
        "Когда-нибудь отправлю тебе курс валют!",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(Text(text="Перевод", text_ignore_case=True), state=None)
async def translate(message: Message):
    await message.answer(
        "Когда-нибудь отправлю тебе перевод!",
        reply_markup=ReplyKeyboardRemove()
    )
