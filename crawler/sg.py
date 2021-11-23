import requests
from bs4 import BeautifulSoup


class SgCrawler:
    host: str = 'https://stopgame.ru'
    news_dir: str = '/news'

    def get_response(self) -> BeautifulSoup:
        html: requests.Response = requests.get(self.host + self.news_dir)
        bs: BeautifulSoup = BeautifulSoup(html.text, 'lxml')
        return bs

    def get_last_key(self) -> str | None:
        bs: BeautifulSoup = self.get_response()
        last_news: list = bs.select(
            '.items > div.item.article-summary'
        )
        last: BeautifulSoup = last_news[0]

        last_key: str = last.attrs['data-key']
        return last_key

    def get_last_url(self) -> str | None:
        bs: BeautifulSoup = self.get_response()
        last_news: list = bs.select(
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







