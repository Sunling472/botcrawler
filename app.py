import asyncio
import multiprocessing as mp
# from aiogram import executor
import sys

from aiogram.types import BotCommand

from loader import dp, pars, bot
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from handlers.users.stop import register_handler_stop
# from utils.set_bot_commands import set_default_commands


async def set_commands(bot):
    commands: list[BotCommand] = [
            BotCommand(command='start', description='Запустить бота'),
            BotCommand(command='help', description='Вывести справку'),
            BotCommand(command='stop_crawler', description='Остановить crawler')
        ]
    await bot.set_my_commands(commands)



async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


async def main(dp, bot):
    await on_startup_notify(dp)

    #   handlers_register
    register_handler_stop(dp)

    await set_commands(bot)
    await dp.start_polling()


# def bot_start():
#     executor.start_polling(dp, on_startup=on_startup)


# def pars_start():
#     pars.parse_start()


if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


if __name__ == '__main__':
    asyncio.run(main(dp, bot))
    # executor.start_polling(dp, on_startup=on_startup)

    # with mp.Pool(2) as pool:
    #     bs.start()
    #     ps.start()
