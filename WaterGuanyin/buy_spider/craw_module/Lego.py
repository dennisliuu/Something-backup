#-*-coding:utf-8-*-
import requests, re, json
from bs4 import BeautifulSoup

class Lego:

    def __init__(self):
        # self.url = url
        self.session = requests.Session()

    def get_single_page(self, url):
        self.url = url
        data = self.crawler_exec()

        return data
    def get_price(self, res):
        "return product price"
        print(res.text)
        self.soup = BeautifulSoup(res.text, 'lxml')
        price_ele = self.soup.find('span', {'class': re.compile('ProductPrice.+')})
        if price_ele is None:
            return -1
        r = re.compile(r'[0-9]+\.[0-9]+')
        result = r.search(price_ele.text)
        if result:
            return result.group()
        return -1

    def get_main_images(self):
        "return product image"
        image_eles = self.soup.find_all('img', re.compile('Thumbnail__Image.+'))
        result = []
        for ele in image_eles:
            result.append(ele.attrs['src'])
        return result

    def get_content_images(self):
        main_contetn_ele = self.soup.find('div', {'class': re.compile('ProductDynamicContent.+')})
        if main_contetn_ele is None:
            return -1
        picture_parents_ele = main_contetn_ele.find_all('picture', {'class': re.compile('HeroBannerstyles__HeroPicture.+')})
        result_list = []
        for par_ele in picture_parents_ele:
            source_eles = par_ele.find_all('source')
            for source in source_eles:
                result_list.append(source.attrs['srcset'])
        return result_list

    def get_tag(self):
        result_list = []
        for item_ele in self.soup.find_all('span', {'class': re.compile('ProductBadge__StyledBadge.+')}):
            result_list.append(item_ele.text)

        return result_list

    def get_title(self):
        title_ele = self.soup.find('h1', {'itemprop': 'name'})
        return title_ele.text

    def get_specifications(self):
        result = {}
        content_ele = self.soup.find('div', {'class': re.compile('ProductFeaturesstyles__Copy.+')})

        content_text = content_ele.text
        result.update({'main': content_text})
        bullet_ele = self.soup.find('div', {'class': re.compile('ProductFeaturesstyles__BulletText.+')})
        if bullet_ele is None:
            return -1
        bullet_text = []

        for li_ele in bullet_ele.find_all('li'):
            bullet_text.append(li_ele.text)
        result.update({'bullet': bullet_text})
        cta_ele = self.soup.find('div', {'class': re.compile('ProductFeaturesstyles__Cta.+')})
        try:
            cta_img_ele = cta_ele.find('img')
            result.update({'cta_img': cta_img_ele.attrs['src']})
        except Exception as e:
            print(str(e))
        return result

    def get_currency(self, res):
        "return product currency"
        self.soup = BeautifulSoup(res.text, 'lxml')
        if self.soup.find('meta', property="product:price:currency")["content"] == "":
            return -1
        return self.soup.find('meta', property="product:price:currency")["content"]

    def crawler_exec(self):
        # 回傳 圖片、說明、價格、文字、幣別的Json
        res = self.session.get(self.url)
        price = self.get_price(res)
        title = self.get_title()
        main_images = self.get_main_images()
        content_images = self.get_content_images()
        # tags = self.get_tag()
        spec = self.get_specifications()

        # currency
        currency = self.get_currency(res)

        key_list = ['title', 'price', 'tags', 'colors', 'size', 'main_images', 'content_images', 'currency', 'url', 'description', 'collection', 'in_stock']
        data = {key: -1 for key in key_list}
        datas = {"price": price,
                 "title": title,
                 "main_images": main_images,
                 "content_images": content_images,
                 "currency": currency
        }
        data.update(datas)
        return data


if __name__ == '__main__':
    url = 'https://www.lego.com/tr-tr/product/land-rover-defender-42110'
    # data = Lego(url).crawler_exec()
    data = Lego().get_single_page(url)
    print(data)

    #save dict as json file
    with open(f"{data['title']}.json", "w") as f:
        f.write(json.dumps(data, sort_keys=True, indent=4))
