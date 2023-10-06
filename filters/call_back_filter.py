from aiogram.filters import BaseFilter
from aiogram.types import Message
from data.get_info import get_subscriptions


async def get_names():
    subscriptions = await get_subscriptions()
    names = list(subscriptions.keys())
    print(names)
    return names


class CallBackFilter(BaseFilter):
    def __init__(self, text: str):
        self.text = text

    async def __call__(self, message: Message) -> bool:
        return self.text in await get_names()
