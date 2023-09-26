from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile

from keyboards.start_kb import start_kb


router = Router()


@router.message(Command('start'))
@router.callback_query(F.data == 'back')
async def start(message: types.Message or types.CallbackQuery):
    keyboard = start_kb()
    image = FSInputFile('img/start.png')
    if type(message) == types.Message:
        name = message.from_user.first_name
        print(message.from_user)

        res = await message.answer_photo(image, caption=f'Main menu. Hello, {name}!', reply_markup=keyboard,)
        # file_ids.append(res.photo[-1].file_id)
    else:
        await message.message.answer_photo(image, caption='Main menu.', reply_markup=keyboard)
