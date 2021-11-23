from aiogram import types


def get_keyboard(user_id: int) -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons: list = [
        types.InlineKeyboardButton(text='Активировать', callback_data=f'activate|{user_id}'),
        types.InlineKeyboardButton(text='Отключить', callback_data=f'deactivate|{user_id}')
    ]
    keyboard.add(*buttons)

    return keyboard
