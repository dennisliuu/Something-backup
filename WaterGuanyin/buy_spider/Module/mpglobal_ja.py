import time
import requests
<<<<<<< HEAD
try:
    import MySQLdb
except:
    import pymysql as MySQLdb
=======
>>>>>>> tiffany
from lxml import etree
from pyquery import PyQuery as pq


class PythonJa:

    # 初始化DB 和 url
    def __init__(self):
        self.url = 'https://mpglobal.donki.com'
        self.search_url = 'https://mpglobal.donki.com/ja/search/0'

    # 解析頁面後回傳
    def __get_page_html(self, url):
        try:
            rs = requests.get(url)
            rs.encoding = 'utf-8'
            html = etree.HTML(rs.text)
            dom = pq(html)
            return dom
        except:
            return False

    # 抓取所有商品url 並執行抓取單頁資料的function
    def get_all_item_url(self):
        dom = self.__get_page_html(self.search_url)
        total_item = dom('text').text()
        total_page = dom('div.paging_product.row')
        total_page = dom('div.paging_product.row li a').eq(len(total_page) - 3).text()
        # print('總共： {}件商品'.format(total_item))
        # print('總共： {}頁'.format(total_page))
        for i in range(1, 2):
            dom = self.__get_page_html(self.search_url + '?&pageNum={}&pageSize=40&orderType=0'.format(i))
            total_item_url = dom('div.col-sm-2.col-md-2.product.product-mini div.default div.product-description a')
            for j in range(0, len(total_item_url)):
                if j % 20 == 0:
                    time.sleep(2)
                url = total_item_url.eq(j).attr('href')
                product_url = self.url + url
                # print(product_url)
                self.get_single_page(product_url)

            self.conn.commit()

    # 抓取 單一商品資料
    def get_single_page(self, url):
        dom = self.__get_page_html(url)
        if not dom:
            return False

        data = dict()
        data['title'] = dom('h1.nameProduct').text().replace("'", '')
        if not data['title']:
            return False

        data['collection'] = dom('div.col-md-12.breadcrumb_ct a').eq(0).text().replace("'", '')
        images = dom('div.imageContent img')
        data['main_image'] = images.eq(0).attr('src')

        data['other_image'] = ''
        for i in range(1, len(images)):
            data['other_image'] += images.eq(i).attr('src') + '\n'

        # 如果商品特價的話 內文在 第６個位置 其他都是在第五個位置
        content_position = 6 if len(dom('div.prob_content.area')) > 6 else 5
        data['content'] = dom('div.prob_content.area').eq(content_position).text().replace("'", '')
        data['price_jp'] = dom('span#Price_JPYEN').text().replace('JP¥ ', '').replace(',', '')
        data['url'] = url

        # 判斷內文中是否還有尺寸資訊 沒有的話抓取內容量
        if data['content'].find('サイズ') != -1:
            data['size'] = dom('p.SPEC').html().split('<br/>')[0].replace('●', '')
            index = 1
            find_size = data['size'].find('サイズ')
            while find_size <= -1:
                data['size'] = dom('p.SPEC').html().split('<br/>')[index].replace('●', '')
                find_size = data['size'].find('サイズ')
                index += 1
        elif data['content'].find('内容量') != -1:
            data['size'] = dom('p.SPEC').html().split('<br/>')[0].replace('●', '')
            index = 1
            find_size = data['size'].find('内容量')
            while find_size <= -1:
                data['size'] = dom('p.SPEC').html().split('<br/>')[index].replace('●', '')
                find_size = data['size'].find('内容量')
                index += 1

        # print(data)
        return data


if __name__ == "__main__":
    test = PythonJa()
    # test.get_single_page('https://mpglobal.donki.com/ja/product/D00005809')
    # test.get_single_page('https://mpglobal.donki.com/ja/product/S00001485')
    test.get_all_item_url()
