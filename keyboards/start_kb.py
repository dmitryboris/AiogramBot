from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    text = ["PS+", "Game Pass", "EA Play"]
    builder.row(
        InlineKeyboardButton(text=text[0], callback_data=text[0]),
        InlineKeyboardButton(text=text[1], callback_data=text[1])
    )
    builder.row(InlineKeyboardButton(text=text[2], callback_data=text[2]))
    return builder.as_markup()
