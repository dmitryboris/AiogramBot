from aiogram import Router, F, types
from aiogram.types import FSInputFile
from keyboards.subscription_info_kb import sub_info
from data.get_info import get_subscriptions_by_own
from aiogram.types.input_media_photo import InputMediaPhoto

router = Router()


@router.callback_query(F.data == "PS+")
async def send_ps_plus_info(callback: types.CallbackQuery):
    subscriptions = await get_subscriptions_by_own('PS')
    kb = sub_info(list(subscriptions.keys()))
    img = FSInputFile('img/ps.jpg')
    text = "PlayStation Plus is Sony's monthly subscription service - required for most online play on " + \
           "PlayStation 4 and PlayStation 5 consoles. It's split into three tiers. \n"
    text += '\n'.join([f'{sub} - {price}$' for sub, price in subscriptions.items()])
    await callback.message.edit_media(InputMediaPhoto(media=img, caption=text), reply_markup=kb)
    # res = await callback.message.answer_photo(img, caption=text, reply_markup=kb)
    # file_ids.append(res.photo[-1].file_id)


@router.callback_query(F.data == "Game Pass")
async def send_ps_plus_info(callback: types.CallbackQuery):
    subscriptions = await get_subscriptions_by_own('XBOX')
    kb = sub_info(list(subscriptions.keys()))
    img = FSInputFile('img/xbox.png')
    text = '\n'.join([f'{sub} - {price}$' for sub, price in subscriptions.items()])
    await callback.message.edit_media(InputMediaPhoto(media=img, caption=text), reply_markup=kb)
    # res = await callback.message.answer_photo(img, caption=text, reply_markup=kb)
    # file_ids.append(res.photo[-1].file_id)


@router.callback_query(F.data == "EA Play")
async def send_ps_plus_info(callback: types.CallbackQuery):
    subscriptions = await get_subscriptions_by_own('EA')
    kb = sub_info(list(subscriptions.keys()))
    img = FSInputFile('img/ea.jpg')
    text = '\n'.join([f'{sub} - {price}$' for sub, price in subscriptions.items()])
    await callback.message.edit_media(InputMediaPhoto(media=img, caption=text), reply_markup=kb)
    # await callback.message.answer_photo(img, caption=text, reply_markup=kb)
