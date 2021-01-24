import time
import requests
from lxml import etree
from pyquery import PyQuery as pq
# pretty print
from pprint import pprint
import re
import json


class Nike:
    def __init__(self):
        self.url = 'https://www.nike.com/'

    # 解析頁面後回傳
    def __get_page_html(self, url):

        # Set domain as US
        cookies = {'CONSUMERCHOICE': 'us/en_us'}
        try:
            rs = requests.get(url, cookies=cookies)
            # print(rs.encoding)
            rs.encoding = 'utf-8'
            html = etree.HTML(rs.text)
            dom = pq(html)
            return dom
        except:
            return False

    def get_single_page(self, url):
        dom = self.__get_page_html(url)
        # print(dom)
        # Find skus
        skus = re.findall(r"\"skus\"\:\[.*\}\]\,\"t", str(dom), flags=re.MULTILINE|re.DOTALL)[0]
        skus = json.loads(skus[7:-3])
        size = []
        for s in skus:
            size.append(s['localizedSize'])

        # Find availableSkus
        availableSkus = re.findall(r"\"availableSkus\"\:\[.*\}\]\,\"p", str(dom), flags=re.MULTILINE|re.DOTALL)[0]
        availableSkus = json.loads(availableSkus[16:-3])
        # print(dom.html().find('classCategories'))
        if not dom:
            return False

        data = dict()
        data['title'] = dom('#pdp_product_title').text().replace("'", "")
        if not data['title']:
            return False

        data['price'] = dom('div.css-b9fpep').eq(0).text().replace('$', '')
        # images = dom('ul.slides li div img')
        # print(images)
        data['main_image'] = dom('.css-viwop1.u-full-width.u-full-height.css-147n82m').attr('src')
        # data['other_images'] = []
        # for i in range(1, len(images)):
        #     data['other_images'].append(images.eq(i).attr('src'))

        data['size'] = dom('.mt4-sm.mb2-sm.mr0-lg.ml0-lg.availableSizeContainer.mt5-sm.mb3-sm.body-baseline-base.css-l8nce8 label').text()
        data['content'] = dom('.description-preview.body-baseline-base.css-1pbvugb').html().replace("'", "")
        data['collection'] = dom('.headline-baseline-base.pb1-sm').eq(0).text()
        data['url'] = url
        data['size'] = size
        # data['availableSkus'] = availableSkus
        # pprint(data)
        # self.insert_or_update_db(data)
        return data


if __name__ == "__main__":
    test = Nike()
    data = test.get_single_page(
        'https://www.nike.com/t/fear-of-god-mens-hooded-bomber-LCjMmR/BV4408-010')

    with open(f"{data['title']}.json", 'w') as f:
        f.write(json.dumps(data, sort_keys=True, indent=4))
    # test.get_single_page('https://www.onitsukatigermagazine.com/store/products/detail.php?product_id=3460&classcategory_id1=7247&category_id=14')
    # test.get_all_collcetion_url()
