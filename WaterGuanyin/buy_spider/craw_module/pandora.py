import time, json, requests, re
from lxml import etree
from pyquery import PyQuery as pq
from pprint import pprint


class Pandora:
    # 初始化DB 和 url
    def __init__(self):

        self.search_url = "https://au.pandora.net/en"
        self.headers = {
            "method": "GET",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed - exchange;v = b3",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7",
            "cache-control": "max-age=0",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                " AppleWebKit/537.36 (KHTML, like Gecko)"
                " Chrome/56.0.2924.87 Safari/537.36"
            ),
        }
        # self.all_item_url = list()

    # 解析頁面後回傳
    def __get_page_html(self, url):
        try:
            rs = requests.get(url, headers=self.headers)
            # print(rs.encoding)
            # rs.encoding = 'Shift_JIS'
            html = etree.HTML(rs.text)
            dom = pq(html)
            return dom
        except:
            return False

    def get_all_collection_url(self):
        dom = self.__get_page_html(self.search_url)
        # print(dom)
        collection_url_list = []
        all_url = dom("li.top-level")
        # print(all_url)
        for i in range(1, len(all_url) - 3):
            collection_url_list.append(all_url.eq(i).children("a").attr("href"))
        # print(collection_url_list)
        collection_url_list = set(collection_url_list)
        self.get_all_item_url(collection_url_list)

    def get_page_item_url_and_return_next_page_url(self, url):
        dom = self.__get_page_html(url)
        item_url = dom("a.thumb-link.thumbnail")
        for index in range(0, len(item_url)):
            self.all_item_url.append(item_url.eq(index).attr("href"))
        print("sleeping")
        time.sleep(2)
        has_next_page = dom("div.infinite-scroll-placeholder").attr("data-grid-url")
        # print(len(set(self.all_item_url)))
        # print(self.all_item_url[len(self.all_item_url)-1])
        return has_next_page

    def get_all_item_url(self, collection_url_list):

        for url in collection_url_list:

            has_next_page = self.get_page_item_url_and_return_next_page_url(url)
            # print(has_next_page)
            while has_next_page:
                has_next_page = self.get_page_item_url_and_return_next_page_url(
                    has_next_page
                )
                # print(has_next_page)

        # self.loop_all_item_url()

    def loop_all_item_url(self):
        for url in set(self.get_all_item_url):
            self.get_single_page(url)

        return True

    def get_single_page(self, url):
        dom = self.__get_page_html(url)
        # print(dom)
        if not dom:
            return False

        data = dict()

        title = re.findall(r"(?:\"product_name\":\[\")(.*?)(?:\")", dom.text(), flags=re.MULTILINE|re.DOTALL)[0]
        if not title:
            return False
        
        price = re.findall(r"(?:\"product_price\":\[\")(.*?)(?:\")", dom.text(), flags=re.MULTILINE|re.DOTALL)
        
        images = re.findall(r"(?:\"product_image_url\":\[\")(.*?)(?:\")", dom.text(), flags=re.MULTILINE|re.DOTALL)
        mainimages = images[0]
        otherimages = images
        for i in range(1, len(otherimages)):
            otherimages.append(i)
        
        colors = re.findall(r"(?:\"product_color\":\[\")(.*?)(?:\")", dom.text(), flags=re.MULTILINE|re.DOTALL)
        color = []
        for i in colors:
            color.append(i)

        sizes = re.findall(r"(?:\"product_size\":\[\")(.*?)(?:\")", dom.text(), flags=re.MULTILINE|re.DOTALL)
        size = []
        for i in sizes:
            size.append(i)

        content = dom('.desktop-detail-text').text()
        
        collection = re.findall(r"(?:\"product_category\":\[\")(.*?)(?:\")", dom.text(), flags=re.MULTILINE|re.DOTALL)[0]

        in_stock = re.findall(r"(?:\"product_instock\":\[\")(.*?)(?:\")", dom.text(), flags=re.MULTILINE|re.DOTALL)[0]

        tags = re.findall(r"(?:\"site_section_levels\":\[\")(.*?)(?:\")", dom.text(), flags=re.MULTILINE|re.DOTALL)
        tag = []
        for i in tags:
            tag.append(i)

        url = re.findall(r"(?:\"product_url\":\[\")(.*?)(?:\")", dom.text(), flags=re.MULTILINE|re.DOTALL)[0]

        # to json
        key_list = [
            "title",
            "price",
            "tags",
            "colors",
            "size",
            "main_images",
            "content_images",
            "currency",
            "url",
            "description",
            "collection",
            "in_stock",
        ]
        data = {key: -1 for key in key_list}
        data["currency"] = "US"
        data["title"] = title
        data["price"] = price
        data["main_images"] = mainimages
        data["content_images"] = otherimages
        data["colors"] = color
        data["size"] = size
        data["description"] = content
        data['collection'] = collection
        data['in_stock'] = in_stock
        data['url'] = url
        data['tags'] = tag
        # pprint(data)
        return data


if __name__ == "__main__":
    test = Pandora()
    data = test.get_single_page(
        "https://au.pandora.net/en/jewellery/bracelets/pandora-moments-harry-potter%2C-golden-snitch-clasp-bangle/598619C00.html"
    )
    # test.get_all_item_url(['https://www.biccamera.com/bc/category/001/150/010/'])
    # test.get_all_collection_url()
    # test.get_all_item_url(['https://www.coach.com/shop/women'])

    # with open(f"{data['title']}.json", "w") as f:
    #     f.write(json.dumps(data, sort_keys=True, indent=4))
