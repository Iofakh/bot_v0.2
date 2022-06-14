from aiogram import Router
from aiogram.dispatcher.filters.text import Text
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup
from aiogram.types import Message

from keyboards.start_kb import start_kb
from keyboards.horoscope_kb import horoscope_kb
from utilits.horoscope import horoscope_pars

router = Router()


class ZodiacSignState(StatesGroup):
    name = State()


@router.message(Text(text="Гороскоп", text_ignore_case=True), state=None)
async def zodiac_sing_check(message: Message, state: FSMContext):
    await state.set_state(ZodiacSignState.name)
    await message.answer(
        "Выбери знак зодиака!",
        reply_markup=horoscope_kb()
    )
    await state.set_state(ZodiacSignState.name)


@router.message(Text(text="Главное меню", text_ignore_case=True))
async def cancel_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer(
        "Вы в главном меню.",
        reply_markup=start_kb(),
    )


@router.message(state=ZodiacSignState.name)
async def current_weather(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    answer = await horoscope_pars(message.text)
    await message.answer(answer,
                         reply_markup=horoscope_kb()
                         )
