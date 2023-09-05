import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types, F
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
    await message.answer('Where are we going?', reply_markup=keyboard)


@dp.message(F.text.lower() == 'left')
async def go_left(message: types.Message):
    await message.reply('Good choice!', reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text.lower() == 'right')
async def go_left(message: types.Message):
    await message.reply('Awesome choice!', reply_markup=types.ReplyKeyboardRemove())


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    print(1)
