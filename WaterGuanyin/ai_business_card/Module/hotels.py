import datetime

import requests
from lxml import etree
from pyquery import PyQuery as pq
from Module import text_fn

class Hotels:

    def __init__(self):
        self.site_url = 'https://www.hotels.com'
        # 預設以 兩個成人只需一個房間為主 只回傳大約十筆
        self.search_url = (
            'https://www.hotels.com/search.do?q-destination='
            '{}&q-check-in={}&q-check-out={}&q-rooms=1&'
            'q-room-0-adults=2&q-room-0-children=0')

    # 解析頁面後回傳
    def __get_page_html(self, url):
        try:
            rs = requests.get(url)
            # print(url)
            html = etree.HTML(rs.text)
            dom = pq(html)
            return dom
        except:
            return False

    def get_single_page(self, location):
        today = datetime.date.today()
        next_day = today + datetime.timedelta(days=1)

        dom = self.__get_page_html(self.search_url.format(
            location, today, next_day))
        # print(dom)
        title_dom = dom("li.hotel section .p-name a")

        address = dom('li.hotel section.hotel-wrap span.address')
        link = dom('figure.image a')
        first_image = dom('img.u-photo.use-bgimage.featured-img-tablet')
        images = dom('.featured-img-desktop')
        # print(len(images))
        hotel_info = list()
        for i in range(0, len(address)):
            hotel_info_dict = dict()
            hotel_info_dict['title'] = title_dom.eq(i).text()
            hotel_info_dict['title'] = text_fn.preg_get_word("(.+)\(.+\)",1,hotel_info_dict['title'])
            hotel_info_dict['address'] = address.eq(i).text()
            hotel_info_dict['link'] = self.site_url + link.eq(i).attr('href')
            # hotel_info_dict['image'] =images.eq(i).attr("src")
            if i == 0:
                hotel_info_dict['image'] = (
                    first_image.eq(i).attr('style')
                    .replace('background-image:url', ''))
            else:
                hotel_info_dict['image'] = (
                    images.eq(i - 1).attr('style').replace('background-image:url', ''))

            new_image = text_fn.preg_get_word("\('(.+)'\)",1,hotel_info_dict['image'])
            hotel_info_dict['image'] = new_image
            hotel_info.append(hotel_info_dict)
        # print(hotel_info)
        return hotel_info


if __name__ == "__main__":
    test = Hotels()
    rs = test.get_single_page("東京")
    print(rs)
