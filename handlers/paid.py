from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from data.add_info import add_order, update_counter
from data.get_info import get_subscription_id
from states.order_sub import OrderSubscription
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()


@router.callback_query(F.data == 'paid', OrderSubscription.choosing_subscription)
async def send_ps_sub(callback: types.CallbackQuery, state: FSMContext):
    img = FSInputFile('img/congratulations.jpg')
    sub_data = await state.get_data()
    sub_name = sub_data['chosen_subscription']
    sub_id = await get_subscription_id(sub_name)
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='Back to main menu', callback_data='back')]])
    await add_order(callback.message.chat.id, sub_id[0])
    await update_counter(callback.message.chat.id)
    await callback.message.answer_photo(photo=img, caption=f'Paid {sub_name}', reply_markup=keyboard)
