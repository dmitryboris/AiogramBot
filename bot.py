import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from handlers import start, subscription_info, subscription
from aiologger.loggers.json import JsonLogger
from dotenv import load_dotenv, find_dotenv
from data import db_session

load_dotenv(find_dotenv())


async def main():
    logger = JsonLogger.with_default_handlers(
        level=logging.INFO,
    )

    bot = Bot(token=os.getenv('TOKEN'))
    db_session.global_init('db/tgbot.sqlite')
    dp = Dispatcher()
    dp.include_routers(start.router, subscription_info.router, subscription.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
