import json
import time

import requests
from pyquery import PyQuery as pq
from lxml import etree

from Module.langconv import Converter


class Jin:

    def __init__(self):
        self.listen_url = 'https://www.jin10.com/flash_newest.js'

        self.headers = {
            'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                           ' AppleWebKit/537.36 (KHTML, like Gecko)'
                           ' Chrome/56.0.2924.87 Safari/537.36')
        }

        self.news = None

    def get_news(self):
        rs = requests.get(self.listen_url
                          , headers=self.headers)
        rs.encoding = 'utf-8'
        news = json.loads(rs.text.replace('var newest = ', '').
                          replace(';', ''))
        return news

    def init_news(self):
        news = self.get_news()
        self.news = dict()
        i = 0
        for v in news:
            if (v['time'] not in self.news.keys()
                    and 'content' in v['data'].keys()):
                content = v['data']['content']
                self.news[v['time']] = (
                    Converter('zh-hant').convert(content))
                i += 1
            if i > 8:
                break
        # print(self.news)

    def listen_web_get_news_return(self):

        while True:

            news = self.get_news()

            if (news[0]['time'] not in self.news.keys()
                    and 'content' in news[0]['data'].keys()):
                self.init_news()

            time.sleep(5)


if __name__ == "__main__":

    test = Jin()
    test.init_news()
    test.listen_web_get_news_return()
