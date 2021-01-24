import time, json
import requests
from lxml import etree
from pyquery import PyQuery as pq
#from config import db


class Biccamera:

    # 初始化DB 和 url
    def __init__(self):

        self.url = 'https://www.biccamera.com/bc/main/'
        self.search_url = 'https://www.biccamera.com/bc/c/contents/sitemap/index.jsp'
        self.next_page_url = '?p={}#bcs_resultTxt'

    # 解析頁面後回傳
    def __get_page_html(self, url):
        try:
            rs = requests.get(url)
            #print(rs.encoding)
            rs.encoding = 'Shift_JIS'
            html = etree.HTML(rs.text)
            dom = pq(html)
            return dom
        except:
            return False

    def get_all_collection_url(self):
        dom = self.__get_page_html(self.search_url)
        collection_url_list = []
        all_url = dom('div.block4 ul li a')
        for i in range(0, len(all_url)):
            collection_url_list.append(all_url.eq(i).attr('href'))
        print(collection_url_list)
        self.get_all_item_url(collection_url_list)

    def get_all_item_url(self, collection_url_list):
        item_url = []
        for url in collection_url_list:
            # print(url)
            dom = self.__get_page_html(url)
            total_page = int(dom('span.bcs_last').text())
            for j in range(1, total_page + 1):
                # print(j)
                dom = self.__get_page_html(url + self.next_page_url.format(j))
                url_total = dom('div.bcs_listItem ul li p a.cssopa')
                for k in range(0, len(url_total)):
                    url = url_total.eq(k).attr('href')
                    print(url)
                    item_url.append(url)
                print("sleeping...")
                time.sleep(2)
            print("sleeping...")
            time.sleep(2)
        # print(len(item_url))
        # print(len(set(item_url)))
        self.loop_all_item_url(item_url)

    def loop_all_item_url(self, item_url):
        for url in item_url:
            self.get_single_page(url)
        return True

    def get_single_page(self, url):
        dom = self.__get_page_html(url)
        # print(dom)
        if not dom:
            return False

        data = dict()
        title = dom('h1#PROD-CURRENT-NAME').text().replace("'", '')
        if not title:
            return False
        price = dom('td.bcs_price p strong').text().replace('円', '').replace(',', '')
        images = dom('li a.bcs_inline img')
        mainimage = images.eq(0).attr('src').split('?')[0] + '?sr.dw=320&sr.dh=320&sr.jqh=60&sr.mat=1'
        otherimage = []
        for i in range(1, len(images)):
            otherimage.append(images.eq(i).attr('src').split('?')[0] + '?sr.dw=320&sr.dh=320&sr.jqh=60&sr.mat=1')
        content = dom('div#bcs_feature').html().replace("'", '') + dom('div#bcs_detail').html().replace("'", '')
        instock = 1 if dom('td.bcs_stock p span.label_green').text() == '在庫あり' else 0
        collection = dom('div.bcs_breadcrumb ul li a span').eq(len(dom('div.bcs_breadcrumb ul li a')) - 1).text()

        # to json        
        key_list = ['title', 'price', 'tags', 'colors', 'size', 'main_images', 'content_images', 'currency', 'url', 'description', 'collection', 'in_stock']
        data = {key: -1 for key in key_list}
        data['title'] = title
        data['price'] = price
        data['main_images'] = mainimage
        data['other_images'] = otherimage
        data['description'] = content
        data['in_stock'] = instock
        data['collection'] = collection
        data['currency'] = 'JP'
        return data


if __name__ == "__main__":
    test = Biccamera()
    data = test.get_single_page('https://www.biccamera.com/bc/item/6942366/')
    # test.get_single_page('https://www.biccamera.com/bc/item/7212446/')
    # test.get_all_item_url(['https://www.biccamera.com/bc/category/001/150/010/'])
    # print(test.get_all_collection_url())

    with open(f"{data['title']}.json", "w") as f:
        f.write(json.dumps(data, sort_keys=True, indent=4))