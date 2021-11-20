import requests
from bs4 import BeautifulSoup
from utils.db_api.base import PostDb


class SgCrawler:
    host: str = 'https://stopgame.ru'
    news_dir: str = '/news'
    last_key: str

    def __init__(self):
        self.html: requests.Response = requests.get(self.host + self.news_dir)
        self.bs: BeautifulSoup = BeautifulSoup(self.html.text, 'lxml')
        self.last_news: list = self.bs.select(
            '.items > div.item.article-summary'
        )
        self.last: BeautifulSoup = self.last_news[0]

    def get_last_key(self):
        last_key: str = self.last.attrs['data-key']
        return last_key

    def get_last_url(self):
        last_url: str = self.last.a['href']
        full_url: str = self.host + last_url
        return full_url

    def parse_one_news(self, url: str):

        one_news_html: requests.Response = requests.get(url)
        on_bs: BeautifulSoup = BeautifulSoup(one_news_html.text, 'lxml')

        title: str = on_bs.h1.text
        body: list = on_bs.select('section.article')
        text_list: list = []

        for t in body:
            text_list.append(t.text)

        print(title)
        for t in text_list:
            print(t)
        print(url)
        return title, text_list, url

db = PostDb()

sg = SgCrawler()
url: str = sg.get_last_url()
title, p_list, url = sg.parse_one_news(url)





