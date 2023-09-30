from aiogram import Router, F, types
from aiogram.types import FSInputFile

from data.get_info import get_user

router = Router()


@router.callback_query(F.data == 'cabinet')
async def start(callback: types.CallbackQuery):
    keyboard = None
    image = FSInputFile('img/start.png')
    info = await get_user(callback.from_user.id)
    print(info)
    caption = ('Cabinet' + '\n' + f'Name: {info[1]}' + '\n' + f'Count of orders: {info[2]}')
    await callback.message.answer_photo(image, caption=caption)
