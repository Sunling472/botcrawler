from bs4 import BeautifulSoup
import requests
import time


from utils.db_api.base import add_news, get_last_post_number

# def parse_news():
#     is_parse: bool = True
#     all_news: str = '/news'
#     last_news_num = get_last_post_number()
#     nm: int = last_news_num + 1
#     sg_url: str = 'https://stopgame.ru'
#
#     while is_parse:
#
#         sg_url_html: str = requests.get(sg_url + all_news).text
#         bs: BeautifulSoup = BeautifulSoup(sg_url_html, 'lxml')
#
#         last_news: BeautifulSoup = bs.find('div', attrs={'class': 'item article-summary', 'data-key': str(nm)})
#
#         if last_news is not None:
#             title: BeautifulSoup = last_news.find('div', attrs={'class': 'caption caption-bold'}).a
#             link: BeautifulSoup = title['href']
#             url_link: str = sg_url + str(link)
#
#             add_news(title.text, url_link, nm)
#
#             print(nm)
#             nm += 1
#
#         time.sleep(5)


class SpiderSg:

    def __init__(self):
        self.is_run: bool = True
        self.all_news_pref: str = '/news'
        self.last_news_num = get_last_post_number()
        self.nm: int = self.last_news_num + 1
        self.sg_url: str = 'https://stopgame.ru'

    def parse_start(self):

        print('Crawler is run.')
        while self.is_run:
            sg_url_html: str = requests.get(self.sg_url + self.all_news_pref).text
            bs: BeautifulSoup = BeautifulSoup(sg_url_html, 'lxml')

            last_news: BeautifulSoup = bs.find('div', attrs={'class': 'item article-summary', 'data-key': str(self.nm)})
            if last_news is not None:
                title: BeautifulSoup = last_news.find('div', attrs={'class': 'caption caption-bold'}).a
                link: BeautifulSoup = title['href']
                url_link: str = self.sg_url + str(link)

                add_news(title.text, url_link, self.nm)
                self.nm += 1

            time.sleep(5)

    def set_is_run(self, is_run: bool):
        self.is_run = is_run

    def parse_stop(self):
        self.set_is_run(False)
        print('Crawler is stop.')


# parser: SpiderSg = SpiderSg()
# parser.parse_start()
