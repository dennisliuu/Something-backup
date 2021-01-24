import time

import requests
from lxml import etree
from pyquery import PyQuery as pq
from moudles import text_fn

class HouseSpider:

    def __init__(self):
        self.search_url = 'https://www.591.com.tw/index.php?module=shop&action=detailHouse&cate_id=2&firstRow={}&totalRows={}&shop_id={}&_={}'
        self.headers = {
            'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        }

    def get_page_dom(self, url):
        try:
            r = requests.Session()
            rs = r.get(url, headers=self.headers)
            html = etree.HTML(rs.text)
            dom = pq(html)
            return dom
        except:
            return False

    @staticmethod
    def parse_url_return_user_id(url):
        user_id = url.replace('https://www.591.com.tw/broker', '').split('?')[0]
        return user_id


    def parse_page_info_return_dict(self, page_start, page_total, user_id):
        search_url = self.search_url.format(page_start, page_total, user_id,time.time())
        dom = self.get_page_dom(search_url)
        # print(dom)
        house = dom('div.list-info a img')
        if not house:
            return False, 0
        house_info = dom('div.list-info span')
        house_price = dom('div.list-info b')
        li_list = dom("div.list-info li")
        a_list = dom("div.list-info li a")
        house_list = list()
        info_index = 0
        for i in range(0, len(house)):
            house_dict = dict()

            house_dict['address'] = (house_info.
                                     eq(info_index).
                                     text().
                                     split('\n')[0])
            if house_info.eq(info_index). text().find('開放式格局') != -1:

                house_dict['size'] = (house_info.
                                      eq(info_index).
                                      text().
                                      split('\n')[1].
                                      split('開放式格局')[1].
                                      replace('，', '').
                                      replace('坪', ''))
            elif house_info.eq(info_index). text().find('店面') != -1:
                house_dict['size'] = (house_info.
                                      eq(info_index).
                                      text().
                                      split('\n')[1].
                                      split('店面')[1].
                                      replace('，', '').
                                      replace('坪', ''))
            elif house_info.eq(info_index).text().find('土地') != -1:
                house_dict['size'] = (house_info.
                                      eq(info_index).
                                      text().
                                      split('\n')[1].
                                      split('土地')[1].
                                      replace('，', '').
                                      replace('坪', ''))
            elif house_info.eq(info_index).text().find('廠房') != -1:
                house_dict['size'] = (house_info.
                                      eq(info_index).
                                      text().
                                      split('\n')[1].
                                      split('廠房')[1].
                                      replace('，', '').
                                      replace('坪', ''))
            elif house_info.eq(info_index).text().find('辦公') != -1:
                house_dict['size'] = (house_info.
                                      eq(info_index).
                                      text().
                                      split('\n')[1].
                                      split('辦公')[1].
                                      replace('，', '').
                                      replace('坪', ''))
            elif house_info.eq(info_index).text().find('商辦') != -1:
                house_dict['size'] = (house_info.
                                      eq(info_index).
                                      text().
                                      split('\n')[1].
                                      split('商辦')[1].
                                      replace('，', '').
                                      replace('坪', ''))
            elif house_info.eq(info_index).text().find('其他') != -1:
                house_dict['size'] = (house_info.
                                      eq(info_index).
                                      text().
                                      split('\n')[1].
                                      split('其他')[1].
                                      replace('，', '').
                                      replace('坪', ''))
            elif house_info.eq(info_index).text().find('住辦') != -1:
                house_dict['size'] = (house_info.
                                      eq(info_index).
                                      text().
                                      split('\n')[1].
                                      split('住辦')[1].
                                      replace('，', '').
                                      replace('坪', ''))
            else:
                house_dict['size'] = (house_info.
                                      eq(info_index).
                                      text().
                                      split('\n')[1].
                                      split('廳')[1].
                                      replace('，', '').
                                      replace('坪', ''))

            house_dict['image'] = house.eq(i).attr('src')
            house_dict['type'] = '中古屋'
            house_dict['room_num'] = text_fn.preg_get_word("(\d*)房\d*廳", 1, li_list.eq(i).html())
            house_dict['rest_num'] = text_fn.preg_get_word("\d*房(\d*)廳", 1, li_list.eq(i).html())
            house_dict['link'] = a_list.eq(i).attr('href')
            house_dict['price'] = int(
                house_price.eq(i).text().replace(',', '') + '0000')
            print(house_dict)
            house_list.append(house_dict)
            info_index += 2

        total_house = dom('a.pageNum-form')
        if total_house:
            total_house = (total_house.eq(0).attr('onclick')
                           .replace('jsHousePage(', '')
                           .replace(')', '').split(',')[1])

        return house_list, total_house

    def parse_all_item_info_return_dict(self, url):
        user_id = HouseSpider.parse_url_return_user_id(url)
        result, total_house = self.parse_page_info_return_dict(1, 100, user_id)
        if not result:
            return False

        if total_house:

            page_start_num = 6
            while page_start_num < int(total_house):
                res, _ = self.parse_page_info_return_dict(page_start_num, total_house, user_id)
                if res == False:
                    break
                for r in res:
                    result.append(r)
                page_start_num += 6
                time.sleep(2)
        print(result)
        return result


if __name__ == '__main__':
    test = HouseSpider()
    test.parse_all_item_info_return_dict('https://www.591.com.tw/broker6354')
