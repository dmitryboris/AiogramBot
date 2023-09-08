from aiogram import Router, F, types
from aiogram.types import FSInputFile
from keyboards.subscription_info_kb import sub_info

router = Router()


@router.callback_query(F.data == "PS+")
async def send_ps_plus_info(callback: types.CallbackQuery):
    subscriptions = {
        "Essential": 100,
        "Extra": 200,
        "Deluxe": 300
    }
    kb = sub_info(list(subscriptions.keys()))
    img = FSInputFile('img/ps.jpg')
    text = '\n'.join([f'{sub} - {price}' for sub, price in subscriptions.items()])
    res = await callback.message.answer_photo(img, caption=text, reply_markup=kb)
    # file_ids.append(res.photo[-1].file_id)


@router.callback_query(F.data == "Game Pass")
async def send_ps_plus_info(callback: types.CallbackQuery):
    subscriptions = {
        "PC": 100,
        "Console": 200,
        "Ultimate": 400
    }
    kb = sub_info(list(subscriptions.keys()))
    img = FSInputFile('img/xbox.png')
    text = '\n'.join([f'{sub} - {price}' for sub, price in subscriptions.items()])

    res = await callback.message.answer_photo(img, caption=text, reply_markup=kb)
    # file_ids.append(res.photo[-1].file_id)


@router.callback_query(F.data == "EA Play")
async def send_ps_plus_info(callback: types.CallbackQuery):
    subscriptions = {
        "EA Play Plus": 100,
        "EA Play Pro": 400
    }
    kb = sub_info(list(subscriptions.keys()))
    img = FSInputFile('img/ea.jpg')
    text = '\n'.join([f'{sub} - {price}' for sub, price in subscriptions.items()])

    await callback.message.answer_photo(img, caption=text, reply_markup=kb)
