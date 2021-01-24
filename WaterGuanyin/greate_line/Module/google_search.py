from queue import Queue
import requests
from pyquery import PyQuery as pq
from lxml import etree
from Module import net_fn
from Module import text_fn
from threading import Thread
import logging
logger = logging.getLogger('chardet.charsetprober')
logger.setLevel(logging.INFO)
class GoogleSpider:

    def __init__(self, proxy=None):
        self.Net = net_fn.Net()
        self.proxy = None
        if proxy != None:
            self.proxy = {
                'http': proxy
            }

        self.search_url = 'https://www.google.com/search?q={}&ved={}&start={}'

        self.headers = {
            'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                           ' AppleWebKit/537.36 (KHTML, like Gecko)'
                           ' Chrome/56.0.2924.87 Safari/537.36')
        }
    def Check_IP_Alive(self):
        rs = self.search_with_key_word('inurl:"b374k.php"',1)
        if rs is None:
            return False
        return True
    def search_with_key_word(self, keyword, page_number=1):
        title = dict()
        # for p in range(1, page_number + 1):
        page = 0 + (10 * (page_number - 1))
        rs = requests.get(self.search_url.format(keyword,page_number, page)
                          , headers=self.headers,timeout=2
                          , proxies=self.proxy)
        rs.encoding = 'utf-8'
        html = etree.HTML(rs.text)
        dom = pq(html)
        page_title = dom('h3.LC20lb')
        # print(rs.text)
        if not page_title:
            return None
        for index in range(0, len(page_title)):
            title[page_title.eq(index).text()] = (
                page_title.eq(index).parent("a").attr('href'))
        return title
        # print(title)
    def Search_Keyword_And_Decode(self,keyword,max_page,report_fn=None):
        #抓取google
        print("Start_Google_:{}".format(keyword))
        Que_Pool = Queue()
        for n in range(max_page):
            p = n + 1
            rs = self.search_with_key_word(keyword,p)
            if rs is None:
                print("SearchFail! IP Bad!")
                break
            for title in rs:
                # print(rs)
                url = rs[title]
                Que_Pool.put(url)
            print("Page:{} Done!".format(p))


        Thread_Num = 150
        print("Ready_Decode_Thread:{}".format(Thread_Num))
        Decode_Thread_list = []

        end_line = []
        for n in range(Thread_Num):
            t = Thread(target=self.Get_Page_Line_fn,args=[Que_Pool,end_line,report_fn])
            Decode_Thread_list.append(t)
            t.start()
        for t in Decode_Thread_list:
            t.join()
            # print("解析線程尚有 {} / {}".format())
        # print(end_line)
        return end_line
    def Search_Result_Decode(self,result_list):
        end_line = []
        for title in result_list:
            link = result_list[title]
            try:
                line_list = self.Get_Page_Line(link)
            except:
                print("{} Error!!".format(link))
                continue
            for lin in line_list:
                if lin not in end_line:
                    end_line.append(lin)
        # print(end_line)
        return end_line
    def Get_Page_Line_fn(self,que,end_line,report_fn=None):
        while que.qsize() > 0:
            url = que.get()
            if report_fn is not None:
                report_fn("正在處理:{}".format(url))
            try:
                line_list = self.Get_Page_Line(url)
            except:
                # print("{}=>Error!".format(url))
                continue
                pass
            for lin in line_list:
                if lin not in end_line:
                    end_line.append(lin)

    def Get_Page_Line(self,url):
        head = "Connection: keep-alive###Cache-Control: max-age=0###Upgrade-Insecure-Requests: 1###User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36###Sec-Fetch-User: ?1###Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3###Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"

        rs = self.Net.Get(url,header_string=head)
        data = rs.text
        data = data.lower()#全小寫
        Line_List = []
        Line_Preg_List = []
        Line_Preg_List.append("line\s:([a-zA-Z\d]+)")
        Line_Preg_List.append("line id([a-zA-Z\d]+)")
        Line_Preg_List.append("line.+(@[a-zA-Z\d]{7})")
        Line_Preg_List.append("line:([a-zA-Z\d]{5,20})")
        Line_Preg_List.append("09[\d]{8}")
        # print(data)
        # print(line_preg_rs)

        exclude_list = ["@keyfram","@context"]
        for preg in Line_Preg_List:
            line_preg_rs = text_fn.preg_get_word(preg, "all", data)
            if line_preg_rs == "empty_data":
                continue

            for n in line_preg_rs:
                n = n.strip()
                if "<"  in n:
                    new_n = text_fn.preg_get_word("<.+>([a-zA-Z\d]{5,20})<\/.+>", 1, n)
                    if new_n == "empty_data":
                        continue
                    n = new_n
                # n = n.replace(":", "")
                # n = n.replace("：", "")
                if n in exclude_list:
                    continue
                if n not in Line_List:
                    Line_List.append(n)
        # print(Line_List)
        # print(data)
        return Line_List


if __name__ == "__main__":

    test = GoogleSpider()
    # rs_list = test.search_with_key_word('台北市 中正區 冷凍工廠 "line:"', 2)
    # test.Search_Result_Decode(rs_list)
    # test.Search_Keyword_And_Decode("台北市 中正區 冷凍設備 \"line:\"",10)
    test.Check_Be_Ban()
    # test.Get_Page_Line("https://www.ec-fun.com/news/ins.php?index_id=76")