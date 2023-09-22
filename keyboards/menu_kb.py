from aiogram.types import MenuButton
from aiogram.types.menu_button_web_app import MenuButtonWebApp


def menu():
    builder = MenuButtonWebApp
    builder.add(MenuButton(type='web_app', text='/back to main menu'))
    return builder
