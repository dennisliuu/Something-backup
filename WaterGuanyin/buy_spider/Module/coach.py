import time
import requests
from lxml import etree
from pyquery import PyQuery as pq


class Coach:
    # 初始化DB 和 url
    def __init__(self):
        self.search_url = 'https://www.coach.com/shop/women'
        self.headers = {
            'method': 'GET',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed - exchange;v = b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
            'cache-control': 'max-age=0',
            'cookie': 'dw=1; __cfduid=dc348069225ff4c55230230200739a34f1574478020; sid=72V1SiIBGELmjGkQ1pCxUYd1uciCPz5l7m4; dwanonymous_619c28b541896bc8ab17cc1fe5a7a6eb=aba0zxeKL9RyQ8Mphry0hXUFPd; dwac_bcZeEiaaiebBkaaade912XuskV=72V1SiIBGELmjGkQ1pCxUYd1uciCPz5l7m4%3D|dw-only|||USD|false|US%2FEastern|true; __cq_dnt=0; dw_dnt=0; dwsid=BjiLzlrfNhxenTt5XhC3Jm4oR0z64RA7Vn_s6mrYh1Z9nxRN8V91SzecDLbnrLumZXpojqwVzYNngyOrM_DniQ==; optimizelyEndUserId=oeu1574478022589r0.5686259077843305; _sdsat_landing_page=https://www.coach.com/static/CStSearchStore.jsp|1574478022649; _sdsat_session_count=1; cqcid=aba0zxeKL9RyQ8Mphry0hXUFPd; _ga=GA1.2.378975455.1574478024; _gid=GA1.2.1909074805.1574478024; _gcl_au=1.1.1278228827.1574478024; apFirstVisit=2019-11-6; _mibhv=anon-1574478027853-1721716120_4580; _micpn=esp:-1::1574478027853; __cq_uuid=670eef40-0d9d-11ea-bebc-91d956cdfd21; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; _scid=dfec6922-99e5-4d12-bbcf-0f1d90868ecc; customer-groups=3949a11305feb3d3411547a209008707; QMReplaySample=false; _fbp=fb.1.1574478028474.25137452; s_vi=[CS]v1|2EEC506605033033-4000119DE00BB771[CE]; _sctr=1|1574438400000; QuantumMetricUserID=d7b9ba82dacf59c5375b7324a35edf48; i10c.ss=1574478059770; i10c.uid=1574478059771:7959; dw=1; _sdsat_traffic_source=https://www.coach.com/sitemap?ctid=site-map; dwsecuretoken_619c28b541896bc8ab17cc1fe5a7a6eb=Uzb0FfAhKGCAkTu64fY62B51JY43YCAX8Q==; bounceClientVisit2277v=N4IgNgDiBcIBYBcEQM4FIDMBBNAmAYnvgO6kB0AxgPYCGFclVAtkSnFREccwKYB2AWj49iAmgCdxASwBuNMCiEixk2fJQgANCHEwQpYozoNqTEAF8gA; QuantumMetricSessionID=ff0276e4aad0088a1c1f286ef9c315f0; __idcontext=eyJjb29raWVJRCI6IjRYQzJUS0NBTFhFTVlUTUFJUFBTQk1RNUFESTVZUVdaU1UzR0taSFIyRDRRPT09PSIsImRldmljZUlEIjoiNFhDMlRLQ0FMU003NFVVTkxQUFNCS1NDQ0g1TkdSN1U1Sk1WTTdPUjVTNkE9PT09IiwiaXYiOiI3VjRYVTdUWVY3NU5RUlJZTFpaUlJZM0xMND09PT09PSIsInYiOjF9; _sdsat_lt_pages_viewed=33; _sdsat_pages_viewed=33; _aa7988=1x51fb; mp_coach_mixpanel=%7B%22distinct_id%22%3A%20%2216e96340e9c672-0b6e125c62a4ba-3961720f-1fa400-16e96340e9d5bd%22%2C%22bc_persist_updated%22%3A%201574478024359%7D; stc115198=env:1574486868%7C20191224052748%7C20191123062501%7C17%7C1047480:20201122055501|uid:1574478028616.2091990374.3242836.115198.1822307618:20201122055501|srchist:1047480%3A1574486868%3A20191224052748:20201122055501|tsa:1574486868442.1806999224.1870284.3151773518202732.:20191123062501; s_sess=%20cmgvo%3DundefinedTyped%252FBookmarkedTyped%252FBookmarkedundefined%3B%20s_cpc%3D0%3B%20s_sq%3D%3B%20s_cc%3Dtrue%3B%20s_ppv%3Dsale%25253Awomen%252526amp%25253B%25252339%25253Bs%252520sale%3B; s_pers=%20s_ccvp%3D%255B%255B%2527Typed%252FBookmarked%2527%252C%25271574478027809%2527%255D%255D%7C1732330827809%3B%20firstVisitDate%3D11%252F23%252F2019%7C1637550057936%3B%20s_nr%3D1574487313447-Repeat%7C1637559313447%3B%20productnum%3D14%7C1577079884301%3B%20s_dfa%3Dcoachprod%7C1574490304569%3B%20s_fid%3D076B82D5837D092F-1E75BCF78A514038%7C1732341305610%3B%20s_vs%3D1%7C1574490305611%3B%20s_dl%3D1%7C1574490305615%3B%20gpv_pn%3Dsale%253Awomen%2526amp%253B%252339%253Bs%2520sale%7C1574490305622%3B; i10c.uservisit=58; i10c.bdddb=c2-97ef2semDP4iSXbVNxn4faE4FqDhn8MKnfKBqq87lyHlHHE8IPr9aK34FQDgFPFsXXF9jma8iuBbIw8aIq0zfKyAnlIHJFQKoXFjjl2LvmCgDNlZDOSzfKBMAqIbGlPFoCA9o8JZdrCbJuBVIyn4foE4FqDhnBHKOXF9yQrvST7gIHE8GJseaK3WPcAR68MKjdnAjlc4irZvqCsVIOn5DN1ALxDgp8MK8kA9og3hgmCGDMDvbJs4aLbBLlIGADMgZv1hPg29dskfDMnVIOHgVF39ArqbKmHKo2PY48T4ir7hqHDaHTn4IJ64FqDgp8MK4wT4olxAGmCgIKBVI1x2aK34FQDgFWcf6XF9jma4irIbIzJVIOn9GF3jAqIz1lxwPXF9jma7drmbIMdkDOszgsy9FlLFEGNOjcp8rp74iRBkGP8asNw5eF3jEuMeADwJsjM4oL1Ejp7gsLIeGJseePA9AqsfLCTFrDA9og2jdrC8YHDaDPQAeR44FQDgFeBCeTA9og3hhv7gsHDaS7YeNF39ArqeADwFoceJjl24jPAbIw8aInFzfKyAnlIgADNFohV4olxEJ; _4c_=dVJdb9s6DP0rgx76FNukLFlygKBwvoYNa7tsw14LW1YWY0lsSG58hyD%2FvZTXFs2ACwQyyXN4QPLkzIadPbIpSiWE1hlKCXrCfts%2Fnk3PzDV1%2BJzYlFnUcluiROS6roxBNJoLIzMllJFVySbsv6CjOZcCeJ6CuExY3dRf2l%2Frr68qeE1LAVNJNNO9EM7sye2Jt%2Bv7zk%2BTZBiG2LSl2dF7SPyu7RJf7m00tAd7vD01dij2%2B1nvniwJP9z9%2BPb489OS%2Brm1RkKWgYQ0pV8kAAAxry1AVSkV5uitO9CWjMLKtYO3jpLFzpH0B6Wp2gb0rjQUOru1zo0MynzTW4reBqOSaetQwjxOYx6dYk61LW3FUqVzJYWU8XhjpYGL11nnq2LxcP9uXX%2BwvWuMf7dzlXifjGnn2jrB5PP3CGMdQ7RUm%2FvES5VnoEBwztMsvS028xnebJt6JvK1nCuRrdZ5wTlAxOd8uVguFzgvqCHHm2KzmoVDdMEZrij6WDyO5%2FufofetoeOHP8ORkWv%2FGKmo1JF5o5H4AlN3zsUI08V7glEELwACe3ScHk7gtZoI%2BF9b3lh4zdK5Fni5XJ4B',
            'referer': 'https://www.coach.com/shop/women-new-arrivals-new-arrivals',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                           ' AppleWebKit/537.36 (KHTML, like Gecko)'
                           ' Chrome/56.0.2924.87 Safari/537.36')
        }
        self.all_item_url = list()

    # 解析頁面後回傳
    def __get_page_html(self, url):
        try:
            rs = requests.get(url, headers=self.headers)
            # print(rs.encoding)
            rs.encoding = 'Shift_JIS'
            html = etree.HTML(rs.text)
            dom = pq(html)
            return dom
        except:
            return False

    def get_all_collection_url(self):
        dom = self.__get_page_html(self.search_url)
        # print(dom)
        collection_url_list = []
        all_url = (
            dom('li.top-level')
        )
        # print(all_url)
        for i in range(1, len(all_url) - 3):
            collection_url_list.append(all_url.eq(i).children("a").attr('href'))
        # print(collection_url_list)
        collection_url_list = set(collection_url_list)
        self.get_all_item_url(collection_url_list)

    def get_page_item_url_and_return_next_page_url(self, url):
        dom = self.__get_page_html(url)
        item_url = dom('a.thumb-link.thumbnail')
        for index in range(0, len(item_url)):
            self.all_item_url.append(item_url.eq(index).attr('href'))

        time.sleep(2)
        has_next_page = (dom('div.infinite-scroll-placeholder').
                         attr('data-grid-url'))
        # print(len(set(self.all_item_url)))
        # print(self.all_item_url[len(self.all_item_url)-1])
        return has_next_page

    def get_all_item_url(self, collection_url_list):

        for url in collection_url_list:

            has_next_page = self.get_page_item_url_and_return_next_page_url(url)
            # print(has_next_page)
            while has_next_page:
                has_next_page = (
                    self.
                    get_page_item_url_and_return_next_page_url(has_next_page)
                )
                # print(has_next_page)

        # self.loop_all_item_url()

    def loop_all_item_url(self):
        for url in set(self.all_item_url):
            self.get_single_page(url)

        return True

    def get_single_page(self, url):
        dom = self.__get_page_html(url)
        # print(dom)
        if not dom:
            return False

        data = dict()
        data['title'] = dom('h1.product-name-desc').text().replace("'", '')
        if not data['title']:
            return False
        data['price_us'] = (dom('span.pdp.list').eq(0).text().
                            replace('$', '').replace(',', ''))
        images = dom('div.element-wrapper img')
        data['main_image'] = images.eq(0).attr('src')
        data['other_images'] = []
        for i in range(1, len(images)):
            data['other_images'].append(images.eq(i).attr('src'))

        data['color'] = []
        color = dom('ul.swatches.swatch-list img')
        for i in range(0, len(color)):
            data['color'].append(color.eq(i).attr('alt'))

        size = dom('select#control-select-size option')
        data['size'] = []
        if size:
            for i in range(1, len(size)):
                data['size'].append(size.eq(i).text())
        data['content'] = (dom('p.editor-notes').text().replace("'", '')
                           + dom('div.pdp-info__details-content').html()
                           .replace("'", ''))
        data['url'] = url
        # print(data)
        return data


if __name__ == "__main__":
    test = Coach()
    # test.get_single_page('https://www.coach.com/coach-central-shopper-tote/78217.html?cgid=women-new-arrivals-new-arrivals&dwvar_color=GMPE4')
    # test.get_single_page('https://www.coach.com/coach-c155-paneled-runner/G4738.html?cgid=men-shoes-new-arrivals&dwvar_color=PDU')
    # test.get_single_page('https://www.coach.com/coach-reversible-shearling-coat/78739.html?dwvar_color=BIC&cgid=men-clothing-outerwear')
    # test.get_single_page('https://www.biccamera.com/bc/item/7212446/')
    # test.get_all_item_url(['https://www.biccamera.com/bc/category/001/150/010/'])
    test.get_all_collection_url()
    # test.get_all_item_url(['https://www.coach.com/shop/women'])
