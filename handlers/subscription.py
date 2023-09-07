from aiogram import Router, F, types
from aiogram.types import FSInputFile
from keyboards.payment_kb import payment_kb

router = Router()


# @router.callback_query(F.data == ["Essential", "Extra", "Deluxe"])
@router.callback_query(F.data == "Essential")
@router.callback_query(F.data == "Extra")
@router.callback_query(F.data == "Deluxe")
async def send_ps_sub(callback: types.CallbackQuery):
    subscriptions = {
        "Essential": 100,
        "Extra": 200,
        "Deluxe": 300
    }
    img = FSInputFile('img/ps.jpg')
    text = f'{callback.data} - {subscriptions[callback.data]}'
    kb = payment_kb()
    await callback.message.answer_photo(img, caption=text, reply_markup=kb)
