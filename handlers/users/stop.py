from aiogram import types, Dispatcher

from loader import dp
from sg import SpiderSg


async def stop(msg: types.Message):
    await msg.answer('Crawler is stop')


def register_handler_stop(dp: Dispatcher):
    dp.register_message_handler(stop, commands='stop_crawler')
