import asyncio
import os

from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher

from app.routers.main import main_router
from app.routers.contacts import contacts_router
from app.routers.faq import faq_router
from app.routers.ticket_status import ticket_status_router
from app.routers.create_ticket import create_ticket_router

from app.database.queue.create_database import create_database


async def main() -> None:
    await create_database()
    load_dotenv(find_dotenv())

    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()

    dp.include_routers(main_router, contacts_router, faq_router, ticket_status_router, create_ticket_router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())