import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import CallbackQuery
from app.handlers import router
from app.database.models import async_main


    
async def main():
    await async_main()
    bot = Bot(token="7802940547:AAHWjtPIx9UfG2bvOUejgOYny44TCVriLvo")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")


