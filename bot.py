import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from handlers import start, subscription_info, subscription, cabinet
from aiologger.loggers.json import JsonLogger
from dotenv import load_dotenv, find_dotenv
from aiogram.types import menu_button_commands
from data import db_session

load_dotenv(find_dotenv())


async def main():
    logger = JsonLogger.with_default_handlers(
        level=logging.INFO,
    )

    bot = Bot(token=os.getenv('TOKEN'), disable_web_page_preview=True)

    await db_session.global_init('db/bot.sqlite')

    description = 'You can buy subscriptions on gaming services. Such as PS+, GamePass and EA PLay'
    await bot.set_my_description(description=description)

    b = menu_button_commands.MenuButtonCommands()
    await bot.set_chat_menu_button(menu_button=b)

    dp = Dispatcher()
    dp.include_routers(start.router, cabinet.router, subscription_info.router, subscription.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
