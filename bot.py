import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import FSInputFile
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiologger.loggers.json import JsonLogger
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

logger = JsonLogger.with_default_handlers(
    level=logging.INFO,
)

# logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()
file_ids = []


def get_keyboard(text: list):
    buttons = [
        [
            types.InlineKeyboardButton(text=text[0], callback_data=text[0]),
            types.InlineKeyboardButton(text=text[1], callback_data=text[1])
        ],
        [types.InlineKeyboardButton(text=text[2], callback_data=text[2])]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


@dp.message(Command('start'))
async def start(message: types.Message):
    text = ["PS+", "Game Pass", "EA Play"]
    kb = get_keyboard(text)
    image = FSInputFile('img/start.png')
    res = await message.answer_photo(image, caption='Main menu', reply_markup=kb)
    file_ids.append(res.photo[-1].file_id)


@dp.callback_query(F.data == "PS+")
async def send_ps_plus_indo(callback: types.CallbackQuery):
    text = ["Essential", "Extra", "Deluxe"]
    kb = get_keyboard(text)
    img = FSInputFile('img/ps.jpg')
    res = await callback.message.answer_photo(img, reply_markup=kb)
    file_ids.append(res.photo[-1].file_id)


@dp.callback_query(F.data == "Game Pass")
async def send_ps_plus_indo(callback: types.CallbackQuery):
    text = ["PC", "Console", "Ultimate"]
    kb = get_keyboard(text)
    img = FSInputFile('img/xbox.png')
    res = await callback.message.answer_photo(img, reply_markup=kb)
    file_ids.append(res.photo[-1].file_id)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    print(1)
