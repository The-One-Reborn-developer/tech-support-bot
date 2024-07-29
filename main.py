import asyncio
import os

from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher

from app.handlers import router


async def main() -> None:
    load_dotenv(find_dotenv())

    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())