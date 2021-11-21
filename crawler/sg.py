import requests
from bs4 import BeautifulSoup
from utils.db_api.base import PostUrlId


class SgCrawler:
    host: str = 'https://stopgame.ru'
    news_dir: str = '/news'


    def __init__(self):
        self.html: requests.Response = requests.get(self.host + self.news_dir)
        self.bs: BeautifulSoup = BeautifulSoup(self.html.text, 'lxml')

    def get_last_key(self) -> str | None:
        last_news: list = self.bs.select(
            '.items > div.item.article-summary'
        )
        last: BeautifulSoup = last_news[0]

        last_key: str = last.attrs['data-key']
        return last_key

    def get_last_url(self) -> str | None:
        last_news: list = self.bs.select(
            '.items > div.item.article-summary'
        )
        last: BeautifulSoup = last_news[0]

        last_url: str = last.a['href']
        full_url: str = self.host + last_url
        return full_url

    def parse_one_news(self, url: str) -> [str]:

        one_news_html: requests.Response = requests.get(url)
        on_bs: BeautifulSoup = BeautifulSoup(one_news_html.text, 'lxml')

        title: str = on_bs.h1.text
        body = on_bs.find('p')

        return title, body.text, url







