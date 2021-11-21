from contextlib import suppress

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from aiogram.utils.exceptions import MessageNotModified

from loader import dp
from utils.db_api.base import UserDb

db: UserDb = UserDb()


def get_keyboard(user_id: int) -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons: list = [
        types.InlineKeyboardButton(text='Активировать', callback_data=f'activate|{user_id}'),
        types.InlineKeyboardButton(text='Отключить', callback_data=f'deactivate|{user_id}')
    ]
    keyboard.add(*buttons)

    return keyboard


def sub(user_id: int):
    if db.is_sub(user_id):
        return 'Активна'
    else:
        return 'Не активна'


def get_hello_text(full_name: str, user_id: int) -> str:
    first_hello_text: str = f'Привет, {full_name}!\n' + 'Вы успешно зарегистрированы!\n'
    hello_text: str = f'Вы уже зарегистрированы, {full_name}\n'
    if db.is_reg(user_id):
        return hello_text

    else:
        return first_hello_text


async def get_sub_status(message: types.Message, user_id: int):
        is_sub: str = sub(user_id)
        sub_text: str = f'Статус вашей подписки: {is_sub}'
        with suppress(MessageNotModified):
            await message.edit_text(sub_text, reply_markup=get_keyboard(user_id))


@dp.message_handler(commands=['start', 'help'])
async def bot_start(message: types.Message):
    user_id: int = message.from_user.id
    full_name: str = message.from_user.full_name
    hello_text: str = get_hello_text(full_name, user_id)
    is_sub: str = sub(user_id)
    sub_text: str = f'Статус вашей подписки: {is_sub}'

    if not db.is_reg(user_id):
        db.add_user(user_id)
        await message.answer(
            text=hello_text + sub_text,
            reply_markup=get_keyboard(user_id)
        )

    else:

        await message.answer(
            text=hello_text + sub_text,
            reply_markup=get_keyboard(user_id)
        )


@dp.callback_query_handler(Text(startswith='activate'))
async def inline_activate_handler(call: types.CallbackQuery):
    user_id: str = call.data.split('|')[1]

    if not db.is_sub(int(user_id)):
        db.set_sub_status(True, int(user_id))
        await get_sub_status(call.message, int(user_id))
        await call.answer()


@dp.callback_query_handler(Text(startswith='deactivate'))
async def inline_deactivate_handler(call: types.CallbackQuery):
    user_id: str = call.data.split('|')[1]

    if db.is_sub(int(user_id)):
        db.set_sub_status(False, int(user_id))
        await get_sub_status(call.message, int(user_id))
        await call.answer()
