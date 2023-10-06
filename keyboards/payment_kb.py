import os
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def payment_kb() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Pay online', url='https://google.com'))
    user_id = os.getenv('ID')
    builder.row(InlineKeyboardButton(text='Seller', url=f"tg://user?id={user_id}"))
    return builder
