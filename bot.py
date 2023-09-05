import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiologger.loggers.json import JsonLogger
from dotenv import load_dotenv

load_dotenv()

logger = JsonLogger.with_default_handlers(
    level=logging.INFO,
)

# logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()

"""@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")"""


@dp.message(Command('weather'))
async def cmd_test1(message: types.Message):
    await message.reply('Not bad')


@dp.message(Command('start'))
async def start(message: types.Message):
    buttons = [
        [types.KeyboardButton(text='Left'),
         types.KeyboardButton(text='Right')
         ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder='Choose your direction'
    )
    await message.answer('Where are we going?')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    print(1)
