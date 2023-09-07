from aiogram import Router, F, types
from aiogram.types import FSInputFile
from keyboards.payment_kb import payment_kb
from filters.emmm import CallBackFilter

router = Router()

subscriptions = {
    "Essential": 100,
    "Extra": 200,
    "Deluxe": 300,
    "EA Play+": 100,
    "EA Play Pro": 400,
    "PC": 100,
    "Console": 200,
    "Ultimate": 400
}


@router.callback_query(CallBackFilter(F.data))
async def send_ps_sub(callback: types.CallbackQuery):
    img = FSInputFile('img/ps.jpg')
    # img = FSInputFile(f'img/{callback.data.lower()}.jpg')
    text = f'{callback.data} - {subscriptions[callback.data]}'
    kb = payment_kb()
    await callback.message.answer_photo(img, caption=text, reply_markup=kb)
