import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.client import client

load_dotenv()
TG_TOKEN = os.getenv("TG_TOKEN")


async def main():
    bot = Bot(token=TG_TOKEN)
    dp = Dispatcher()
    dp.include_router(client)
    await dp.start_polling(bot)






if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Бот остановился')










