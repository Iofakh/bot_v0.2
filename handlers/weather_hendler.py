from aiogram import Router
from aiogram.dispatcher.filters.text import Text
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup
from aiogram.types import Message

from keyboards.start_kb import start_kb
from keyboards.weather_kb import weather_kb
from utilits.owm_check import owm

router = Router()


class Locality(StatesGroup):
    name = State()


@router.message(Text(text="Погода", text_ignore_case=True), state=None)
async def weather_check(message: Message, state: FSMContext):
    await state.set_state(Locality.name)
    await message.answer(
        "Выбери город!",
        reply_markup=weather_kb()
    )
    await state.set_state(Locality.name)


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


@router.message(state=Locality.name)
async def current_weather(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(await owm(message.text),
                         reply_markup=weather_kb()
                         )
