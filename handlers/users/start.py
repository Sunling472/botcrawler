# import multiprocessing as mp

from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import pars
# from utils.db_api.base import list_base

from loader import dp


class StateUrl(StatesGroup):
    url: str = ''

# def pars_start():
#     pars.parse_start()


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # list_news: list = list_base()
    await message.answer(f"Привет, {message.from_user.full_name}!")

    # ps: mp.Process = mp.Process(target=pars_start)
    # with mp.Pool(2):
    #     ps.start()


