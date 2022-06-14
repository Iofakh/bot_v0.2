import asyncio

from aiogram import Bot, Dispatcher

from handlers import start_heandler, weather_hendler, horoscope_hendler, different_types


# Запуск бота
async def main():
    bot = Bot("5124242670:AAGxOAfvKN5UrTnUlOvP-npY6jpv7qsQOG8")
    dp = Dispatcher()

    dp.include_router(start_heandler.router)
    dp.include_router(weather_hendler.router)
    dp.include_router(horoscope_hendler.router)
    dp.include_router(different_types.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
