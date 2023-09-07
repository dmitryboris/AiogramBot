from aiogram.filters import BaseFilter
from aiogram.types import Message

subscriptions = ["Essential", "Extra", "Deluxe", "PC", "Console", "Ultimate", "EA Play+", "EA Play Pro"]


class CallBackFilter(BaseFilter):
    def __init__(self, text: str):
        self.text = text

    async def __call__(self, message: Message) -> bool:
        return self.text in subscriptions
