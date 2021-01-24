import time

import requests

try:
    import MySQLdb
except:
    import pymysql as MySQLdb
from lxml import etree
from pyquery import PyQuery as pq

from config import db


class OnitsukaTiger:

    # 初始化DB 和 url
    def __init__(self):
        self.url = 'https://www.onitsukatiger.com/jp/ja-jp'
        self.next_page = '?Sort=Featured&page={}'

    # 解析頁面後回傳
    def __get_page_html(self, url):
        try:
            rs = requests.get(url)
            # print(rs.encoding)
            rs.encoding = 'utf-8'
            html = etree.HTML(rs.text)
            dom = pq(html)
            return dom
        except:
            return False

    def get_all_collcetion_url(self):
        dom = self.__get_page_html(self.url)
        collection_url = []
        url = dom('a.dylan-link.col-title')

        for i in range(0, 2):
            collection_url.append(self.url + url.eq(i).attr('href'))
        # print(collection_url)
        self.get_all_item_url(collection_url)

    def get_all_item_url(self, collection_url):
        item_url_list = []
        for url in collection_url:
            i = 0
            dom = self.__get_page_html(url)
            next_page = dom('div.next-page-link.hid')
            while next_page:
                i += 1
                next_page_url = url + self.next_page.format(i)
                dom = self.__get_page_html(next_page_url)
                item_url = dom('li.product-item a')
                for u in range(0, len(item_url)):
                    item_url_list.append(self.url + item_url.eq(u).attr('href'))
                time.sleep(2)
                next_page = dom('div.next-page-link.hid')

        self.get_all_item_detail_url(set(item_url_list))

    def get_all_item_detail_url(self, item_url):
        detail_url = []
        for i, url in enumerate(item_url):
            if i % 20 == 0:
                time.sleep(2)
            dom = self.__get_page_html(url)
            detail_url.append(dom('div.online-stroe-link a').attr('href'))

        self.loop_all_item_detail_url(set(detail_url))

    def loop_all_item_detail_url(self, detail_url):
        for url in detail_url:
            self.get_single_page(url)
        return True

    def get_single_page(self, url):
        dom = self.__get_page_html(url)
        # print(dom)
        # print(dom.html().find('classCategories'))
        if not dom:
            return False

        data = dict()
        data['title'] = dom('div.details_right h3').eq(0).text().replace("'", "")
        if not data['title']:
            return False

        data['price_jp'] = dom('h4.price font').eq(0).text().replace('￥', '').replace(',', '')
        images = dom('ul.slides li div img')
        # print(images)
        data['main_image'] = images.eq(0).attr('src')
        data['other_images'] = []
        for i in range(1, len(images)):
            data['other_images'].append(images.eq(i).attr('src'))

        data['size'] = dom('ul.size_list li').html()
        data['content'] = dom('div.detail_conntent').html().replace("'", "")
        data['collection'] = dom('ol.breadcrumb li a span').eq(len(dom('ol.breadcrumb li a span')) - 1).text()
        data['url'] = url
        # print(data)
        return data


if __name__ == "__main__":
    test = OnitsukaTiger()
    test.get_single_page('https://www.onitsukatigermagazine.com/store/products/detail.php?product_id=1768&classcategory_id1=3749')
    # test.get_single_page('https://www.onitsukatigermagazine.com/store/products/detail.php?product_id=3460&classcategory_id1=7247&category_id=14')
    # test.get_all_collcetion_url()
    # test.get_all_collection_url()
