import json
import time

import requests

try:
    import MySQLdb
except:
    import pymysql as MySQLdb

from lxml import etree
from pyquery import PyQuery as pq

from config import db


class Uniqlo:
    # 初始化DB 和 url
    def __init__(self):
        self.url = 'https://www.uniqlo.com/'
        self.sitemap_url = 'https://www.uniqlo.com/jp/sitemap/'
        self.item_url = 'https://www.uniqlo.com/jp/spa-proxy/catalog/product/details?products={}&review_limit=2'
        self.single_page_headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        self.collection_page_headers = {
            'authority': 'www.uniqlo.com',
            'method': 'GET',
            'path': '',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
            'cache-control': 'max-age=0',
            'cookie': 'BC8C1E91EE176F48C08F50143AC5C61E~YAAQf4pFy04HuDRuAQAAaiD0NgWGgBP8CqjTE9VBa1rp3XpFT/WQiAFMZba6ii9/FokQQO4cXZ8b/R2Lb9TLaI62bYJodvCkqfZIrNFb4gSqtgsujZxWQhSrLXSWxXUQ0u0kvyr+KNvGBwd5VXp63qIGOqABDGCrkt3+oQlHY5OLI/Lrc628gzsE4nv61lyT; _abck=BEB3EE4BEA613D61326F83DE61DD6FA3~0~YAAQf4pFy1oHuDRuAQAALyP0NgK8ltrEDsUOkGOVzmOpwsE9U37TZ9j55a0FKUQ+GIkvjxKsSpHy7ETttAI/Ta85Bjt+r9xEN0mxE7dqrFQw2gNnm305gDzalyhoYQO/T/+qNUmwzn7MiaTGx0gHNRM+/A6iTW9tHtlMLkrKjgcd7IqXUYzLlfDFolTfFMMfHxKYaW8yNaeJAJOY4cquJq4R8DRk39JfXj5tuFFuowj/k6cGiFCMR7COWSo2p9TDqtAp8n/lcF4WopGlDBxQ7zknL+w7f/iY9nVkLul1wI+kiQ==~-1~-1~-1; _gcl_au=1.1.1014953963.1572880000; uqpage=1; _fbp=fb.1.1572880000226.1572553888; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.981126380.1572880000; _gid=GA1.2.151135094.1572880000; _dc_gtm_UA-494938-9=1; ak_bmsc=D6613323BA5904C659BE389E107DA802CB458A7F4B6200007F3EC05DA4FED04F~ple6vfS1WCbKHIgAUi/tT5naWXvqjWUEC0W85eTXczM6ZsFLkWAYlou7VJ8oR/4VxjAFJlk774H8PoJU6J1Cznukqp6bd0Dh6Mr6TYKH5V+QACsFbhtqdjH2GAsErqxX8A1NE6WNYmP5iIWEsukaW6g+zhoLz8MPEp0IiLiYdMReSh6I1sC5o3WLNpqZ09fQQCYNtv/XlrGHPgGgwAd2YhfQ4jxpgXRSE13N9ffhIxstyxs/oM0O23gonxdxh2Z6pU; __lt__cid=d0555a0d-5ed7-45f4-9406-0b7d5973e712; __lt__sid=bc94a9da-f45331dd; snexid=d625e1e8-3a01-43f5-adc4-356aa3a8c34f; bm_sv=5FB769E5DAD48983D4232479BA3F3788~x1Vt1c1Bq8b3bq74107Kgxut/HDrrKx6x7TF6gfGb+RikY1ITtlKyIl6MceCjQyqvitSebvZi1POumrMcDagjexhTRI16YqsOD9HrOwQ2ynrkDx21i6asH56mt1IyDvjQG2IC9mxKW51o+BgoPcQk7XZfV07k1EBvJcjbJNBnqk=; akavpau_www_uniqlo_com=1572880302~id=86466980eaf9b88462f4969f3c8c74f9',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'

        }

    # 解析頁面後回傳
    def __get_page_html(self, url):
        try:
            self.collection_page_headers['path'] = url.replace(self.url, '')
            # print(self.collection_page_headers)
            rs = requests.get(url, headers=self.collection_page_headers)
            rs.encoding = 'utf-8'
            html = etree.HTML(rs.text)
            dom = pq(html)
            return dom
        except:
            return False

    # 取得商品頁面Json後回傳
    def __get_page_res(self, url):

        self.single_page_headers['Referer'] = url
        rs = requests.get(url, headers=self.single_page_headers)
        rs.encoding = 'utf-8'
        if rs.json()['count'] == 0:
            return False
        return rs

    # 抓取所有分類的商品url
    def get_collection_item_url(self):
        # TODO:目前撈回來得是html骨幹而已 沒有資料 還是要用模擬ajax的方法才能抓到分類內所有商品的url
        dom = self.__get_page_html('https://www.uniqlo.com/jp/store/feature/uq/outer/women/')
        # print(dom)

    # 抓取 單一商品資料
    def get_single_page(self, url):
        print(url)
        prodcut_id = url.replace('https://www.uniqlo.com/jp/store/goods/', '').split('-')[0]
        rs = self.__get_page_res(self.item_url.format(prodcut_id))
        if not rs:
            return False
        re_dict = rs.json()
        product_info = re_dict['products'][0]

        data = dict()
        data['title'] = product_info['title'].replace("'", '')
        if not data['title']:
            return False
        data['price_jp'] = product_info['defaultSalePrice']

        data['main_images'] = []
        for image in product_info['images'].keys():
            data['main_images'].append(product_info['images'][image]['main']['path'])

        data['other_images'] = []
        for image in product_info['alternateImages']:
            data['other_images'].append(image['main']['path'])

        data['size'] = []
        for size in product_info['sizesList'].keys():
            data['size'].append(product_info['sizesList'][size]['name'])

        data['colors'] = []
        for color in product_info['allColorsList'].keys():
            data['colors'].append(product_info['allColorsList'][color]['name'])

        data['tags'] = []
        for tag in product_info['tags']:
            data['tags'].append(tag['name'])

        data['content'] = ((product_info['description'] + product_info['handling'] + product_info['materials'])
                           .replace("'", ''))
        data['url'] = url

        # print(data)
        return data


if __name__ == "__main__":
    test = Uniqlo()
    test.get_single_page('774187515555-68')
    test.get_single_page('https://www.uniqlo.com/jp/store/goods/421615-08')
    # test.get_collection_item_url()

