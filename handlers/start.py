from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from keyboards.start_kb import start_kb
from data import db_session
from data.user import User
router = Router()


@router.message(Command('start'))
@router.callback_query(F.data == 'back')
async def start(message: types.Message or types.CallbackQuery):
    keyboard = start_kb()
    image = FSInputFile('img/start.png')
    if type(message) == types.Message:
        name = message.from_user.first_name
        print(message.from_user)
        db_sess = db_session.create_session()
        user_id = message.from_user.id

        if not db_sess.query(User).filter(User.id == user_id).first():
            user = User()
            user.id = user_id
            user.name = name
            db_sess.add(user)
        db_sess.commit()
        res = await message.answer_photo(image, caption=f'Main menu. Hello, {name}!', reply_markup=keyboard)
        # file_ids.append(res.photo[-1].file_id)
    else:
        await message.message.answer_photo(image, caption='Main menu.', reply_markup=keyboard)
