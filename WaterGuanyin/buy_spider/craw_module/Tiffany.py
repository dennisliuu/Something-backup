#-*-coding:utf-8-*-
import requests, re, json
from bs4 import BeautifulSoup


class Tiffany(object):
    def get_single_page(self, url):
        req = requests.get(url).text
        self.soup = BeautifulSoup(req, 'lxml')

        scrt_js = self.soup.find('script', type="application/ld+json").get_text().strip().replace("\n","").replace(" ","").replace('""','\'"')
        # scrt_js = self.soup.find('script', type="application/ld+json").get_text().strip()
        scrt_js = json.loads(scrt_js)
        # print(scrt_js)
        js_info = dict(scrt_js)
        title = js_info["name"]
        price = js_info['offers']["price"]
        currency = js_info['offers']['priceCurrency']
        collection = js_info["category"]
        description = js_info["description"]
        mainimages = js_info['image'].split('&')[0]
        # reformat json
        key_list = ['title', 'price', 'tags', 'colors', 'size', 'main_images', 'content_images', 'currency', 'url', 'description', 'collection', 'in_stock']
        datas = {key: -1 for key in key_list}
        data = {'title': title, 'currency': currency, 'price': price, 'collection': collection, 'description': description, 'main_images': mainimages}
        datas.update(data)
        return datas


if __name__ == "__main__":
    url1 = "https://www.tiffany.com/jewelry/necklaces-pendants/tiffany-t-smile-pendant-35189459/"
    url2 = "https://www.tiffany.com/jewelry/necklaces-pendants/tiffany-t-smile-pendant-35189459/"
    tiffany = Tiffany()
    data = tiffany.get_single_page(url1)
    with open(f"{data['title']}.json", "w") as f:
        f.write(json.dumps(data, sort_keys=True, indent=4))
