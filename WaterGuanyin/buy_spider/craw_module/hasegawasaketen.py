import time
import requests
from lxml import etree
from pyquery import PyQuery as pq


class Hasegawa:
    # 初始化DB 和 url
    def __init__(self):

        self.url = 'https://www.hasegawasaketen.com/eshop/'
        self.change_page_url = '&pageno={}'
        self.index_url = 'https://www.hasegawasaketen.com'

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

    # 抓取所有分類的網址與頁數
    def get_all_collection_url_and_page_num(self):
        dom = self.__get_page_html(self.url)
        collection_page_num = dict()
        collection_url = dom('ul.sitemap li a')
        for i in range(0, len(collection_url)):
            url = collection_url.eq(i).attr('href')
            if url == 'https://www.hasegawasaketen.com/index.html':
                break
            else:
                collection_dom = self.__get_page_html(url)
                total_page = collection_dom('div#pagination_wrap ul li a')
                total_page = total_page.eq(len(total_page) - 2).text()
                if total_page:
                    pass
                else:
                    total_page = 1
                collection_page_num[url] = total_page

        self.get_all_item_url(collection_page_num)

    # 抓取所有商品的url
    def get_all_item_url(self, collection_dict):
        item_url = []
        for key in collection_dict:
            if collection_dict[key] == 1:
                dom = self.__get_page_html(key)
                url_list = dom('div.cart-btn a')
                for i in range(0, len(url_list)):
                    item_url.append(url_list.eq(i).attr('href'))
            else:
                for i in range(1, int(collection_dict[key]) + 1):
                    url = key + self.change_page_url.format(i)
                    dom = self.__get_page_html(url)
                    url_list = dom('div.cart-btn a')
                    for j in range(0, len(url_list)):
                        item_url.append(url_list.eq(j).attr('href'))
        item_url = set(item_url)
        self.__loop_item_url_get_info(item_url)

    def __loop_item_url_get_info(self, item_url_list):
        for index, i in enumerate(item_url_list):
            if index % 20 == 0:
                time.sleep(2)
            self.get_single_page(i)

    # 抓取 單一商品資料
    def get_single_page(self, url):
        print(url)
        dom = self.__get_page_html(url)
        if not dom:
            return False

        data = dict()
        title = dom('section.item_txt h2').text().replace("'", '')
        if not title:
            return False

        size1 = dom('div.item_price table tbody tr td').eq(0).text()
        price1 = (dom('div.item_price table tbody tr td.price').eq(0).text().
                             replace(' 税込', '').replace('¥ ', '').replace(',', ''))

        price2 = (dom('div.item_price table tbody tr td.price').eq(1).text().
                     replace(' 税込', '').replace('¥ ', '').replace(',', ''))
        size2 = dom('div.item_price table tbody tr td').eq(4).text()

        images = dom('section.item_photo img')
        mainimages = self.index_url + images.eq(1).attr('src')

        otherimages = ''
        for i in range(2, len(images)):
            otherimages += self.index_url + images.eq(i).attr('src') + '\n'

        collection = dom('section#topicpath ul li a').eq(2).text()
        content = dom('div#item_additional').text().replace("'", '')

        if price2:
            if price2 != 0:
                price = [price1, price2]
        else:
            price = price1
        
        if size2:
            if size2 is not "":
                size = [size1, size2]
        else:
            size = size1


        #to json 
        #currency = jp
        key_list = ['title', 'price', 'tags', 'colors', 'size', 'main_images', 'content_images', 'currency', 'url', 'description', 'collection', 'in_stock']
        data = {key: -1 for key in key_list}
        data['title'] = title
        data['price'] = price
        data['size'] = size
        data['main_images'] = mainimages
        data['other_images'] = otherimages
        data['collection'] = collection
        data['content'] = content

        return data
        

if __name__ == "__main__":
    test = Hasegawa()
    #test.get_single_page('https://www.hasegawasaketen.com/eshop/products/detail/12943')
    data = test.get_single_page('https://www.hasegawasaketen.com/eshop/products/detail/6847')
    #test.get_all_collection_url_and_page_num()
    print(data)