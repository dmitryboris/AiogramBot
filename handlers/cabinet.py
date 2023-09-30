from aiogram import Router, F, types
from aiogram.types import FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from data.get_info import get_user

router = Router()


@router.callback_query(F.data == 'cabinet')
async def start(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Back to main menu', callback_data='back'))
    image = FSInputFile('img/start.png')
    info = await get_user(callback.from_user.id)
    print(info)
    caption = ('Cabinet' + '\n' + f'Name: {info[1]}' + '\n' + f'Count of orders: {info[2]}')
    await callback.message.answer_photo(image, caption=caption, reply_markup=builder.as_markup())
