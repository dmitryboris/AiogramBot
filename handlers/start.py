from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile, InputMediaPhoto

from keyboards.start_kb import start_kb
from data.add_info import add_user
from data.get_info import get_user


router = Router()


@router.message(Command('start'))
@router.callback_query(F.data == 'back')
async def start(message: types.Message or types.CallbackQuery):
    keyboard = start_kb()
    image = FSInputFile('img/start.png')
    if type(message) == types.Message:
        name = message.from_user.first_name
        print(message.from_user)
        user = await get_user(message.from_user.id)
        if not user:
            await add_user(message.from_user.id, message.from_user.first_name)
        res = await message.answer_photo(image, caption=f'Main menu. Hello, {name}!', reply_markup=keyboard,)
        # file_ids.append(res.photo[-1].file_id)
    else:
        await message.message.edit_media(InputMediaPhoto(media=image, caption='Main menu'), reply_markup=keyboard)
        # await message.message.answer_photo(image, caption='Main menu.', reply_markup=keyboard)
