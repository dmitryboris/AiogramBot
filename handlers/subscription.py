from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, InlineKeyboardButton
from keyboards.payment_kb import payment_kb
from filters.call_back_filter import CallBackFilter
from data.get_info import get_subscriptions
from states.order_sub import OrderSubscription

router = Router()


@router.callback_query(CallBackFilter(F.data)) # ??????? почему проваливается с дата=paid
async def send_ps_sub(callback: types.CallbackQuery, state: FSMContext):
    subscriptions = await get_subscriptions()
    img = FSInputFile(f'img/{callback.data.lower().replace(" ", "")}.jpg')
    text = f'{callback.data} - {subscriptions[callback.data]}'
    builder = payment_kb()
    builder.row(InlineKeyboardButton(text='Pay', callback_data='paid'))
    await callback.message.answer_photo(img, caption=text, reply_markup=builder.as_markup())
    await state.set_state(OrderSubscription.choosing_subscription)
    await state.update_data(chosen_subscription=callback.data)
