import asyncio
from aiogram import types, Bot

from loader import dp, bot
from utils.db_api.base import PostUrlId, FullPosts, UserDb
from crawler.sg import SgCrawler

crawler_sg: SgCrawler = SgCrawler()

posts_url_id_db: PostUrlId = PostUrlId()
full_posts_db: FullPosts() = FullPosts()
users_db: UserDb = UserDb()


def check_new_post(last_id: str, last_post_id: str | None) -> bool | None:
    if last_post_id is None or int(last_id) > int(last_post_id):
        return True
    elif int(last_id) < int(last_post_id):
        return False
    else:
        return None


async def scheduled_news(wait: int):
    while True:

        last_id: str | None = crawler_sg.get_last_key()
        last_url: str | None = crawler_sg.get_last_url()
        last_post_id: str | None = full_posts_db.get_last_fpost_id()

        if check_new_post(last_id, last_post_id):
            title, body, url = crawler_sg.parse_one_news(last_url)

            full_posts_db.add_full_post(title, body, url, int(last_id))
            subs_id: list = users_db.get_subs_id()

            try:
                for sub in subs_id:
                    await bot.send_message(
                        sub,
                        f'<b>{title}</b>\n\n'
                        f'{body}\n\n'
                        f'Подробнее:\n'
                        f'{url}',
                        disable_web_page_preview=True,
                        parse_mode='HTML'
                    )
            except TypeError:
                print('CRAWLER: Ошибка. База пользователей пуста')

        # last_id = None
        # last_url = None
        # last_post_id = None

        await asyncio.sleep(wait)




