from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text

from loader import dp
from utils.db_api.base import UserDb

db: UserDb = UserDb()


def get_keyboard(user_id: int) -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text='Активировать', callback_data=f'activate|{user_id}'))

    return keyboard


def sub(user_id: int):
    if db.is_sub(user_id):
        return 'Активна'
    else:
        return 'Не активна'


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id: int = message.from_user.id
    if db.is_reg(user_id):
        db.add_user(user_id)

        await message.answer(
            f'Привет, {message.from_user.full_name}!\n'
            f'Вы успешно зарегистрированы!\n'
            f'Статус вашей подписки: {sub(message.from_user.id)}',
            reply_markup=get_keyboard(user_id)
        )

    else:
        await message.answer(
            f'Вы уже зарегистрированы, {message.from_user.full_name}\n'
            f'Статус вашей подписки: {sub(message.from_user.id)}',
            reply_markup=get_keyboard(user_id)
        )


@dp.callback_query_handler(Text(startswith='activate'))
async def inline_activate_handler(call: types.CallbackQuery):
    user_id: str = call.data.split('|')[1]
    if db.is_sub(int(user_id)):
        db.set_sub_status(False, int(user_id))
        await call.answer()
    else:
        db.set_sub_status(True, int(user_id))
        await call.answer()
