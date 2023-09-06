from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def sub_info(text: list) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text=text[0], callback_data=text[0]),
        InlineKeyboardButton(text=text[1], callback_data=text[1])
    )
    try:
        builder.row(InlineKeyboardButton(text=text[2], callback_data=text[2]))
    except IndexError:
        pass
    builder.row(InlineKeyboardButton(text='Back to main menu', callback_data='back'))
    return builder.as_markup()
