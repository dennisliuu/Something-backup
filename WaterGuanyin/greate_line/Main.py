import json
import os
import time
from Module import adsl
from Module import WS_UI
from Control import Line_Con
from Module import Browser
from Control import Line_Con
from Module import google_search
class Main:
    def __init__(self):
        self.Browser = Browser.Browser()
        self.WS_UI = WS_UI.WUI("","",exit_time=99999)
        self.Adsl = adsl.Adsl()
        self.Google = google_search.GoogleSpider()

        self.Line = Line_Con.Line("")
        self.Init_WS_fn()
        self.Weboscket_Server()


    def Init_WS_fn(self):
        self.WS_UI.Add_Recv_Msg_Hook("login", self.Line.Start_Line)
        self.WS_UI.Add_Recv_Msg_Hook("Search", self.Search_Google)


        self.Line.WS_Login_Success_Callback = self.Send_Login_Success_Message

    def Search_Process_List(self,msg):
        self.WS_UI.Broadcast("Search_Process",msg)

    def Search_Google(self,client=None,keyword_pack=None,fallback=None):
        # print(keyword_pack)
        keyword_list = []
        for city in keyword_pack['city']:
            # for area in city['area_list']:
            for area in city['city_name']:
                for key in keyword_pack['keyword']:
                    # keyword = "{} {} {} \"line:\"".format(area,city['city_name'],key)
                    keyword = "{} {} {} \"line:\"".format(area,city['area_list'],key)
                    keyword_list.append(keyword)
        print("共產生 {} 組keyword".format(len(keyword_list)))
        end_list = []
        Adsl_Pack = None
        if "adsl" in keyword_pack:
            Adsl_Pack = keyword_pack['adsl']
        if Adsl_Pack != None:
            self.Adsl.set_adsl(Adsl_Pack)
        st = time.time()
        af = 0
        for n,keyword in enumerate(keyword_list):
            stat = False

            print("正在處理:{} / {} 組關鍵字 已費時 {}秒".format(n,len(keyword_list),af))
            if Adsl_Pack != None:
                #檢查ip
                while stat == False:
                    stat = self.Google.Check_IP_Alive()
                    if stat == False:
                        self.Adsl.reconnect()
            report_fn = self.Search_Process_List
            line_list = self.Google.Search_Keyword_And_Decode(keyword,10,report_fn)
            for lin in line_list:
                if lin not in end_list:
                    end_list.append(lin)
            af = st - time.time()
        with open("line_rs.txt",'w',encoding="utf-8") as fp:
            json.dump(end_list,fp)

        self.WS_UI.Broadcast("Line_Search_Report",end_list)
        print("共{}筆".format(len(end_list)))


        # self.Google.set_adsl(Adsl_Pack)
    def Send_Login_Success_Message(self,client):
        self.WS_UI.Send_Order(client,"login_success","")

    def WS_Renew_Friend_List(self,client,msg):
        Friend_List = self.Line.Get_Friend_List(no_ele=1)
        self.WS_UI.Send_Order(client,"Friend_List",Friend_List)


    def Weboscket_Server(self):
        self.WS_UI.Start_WS(start_browser=0)

    def Start(self):
        # Web crab
        # adsl_pack =  {"name": "寬頻連線dyn",
        #             "username": "75871090@hinet.net",
        #             "password": "amufjlzy"}
        # city_pack = {"area_list":["松山區","中山區"],'city_name':"臺北市"}
        # test_keyword_pack = {"city":[city_pack],"keyword":["家事","清潔","傢俱","廚衛","建材"],'adsl':adsl_pack}
        # self.Search_Google(keyword_pack=test_keyword_pack)

        # self.Driver = self.Browser.Init_Browser("")
        # self.Driver.get("chrome-extension://ophjlpahpchlmihnnnihgmmeilfjmjjc/index.html")

        # Line
        self.Line = Line_Con.Line(parse_dir="")
        login_stat = self.Line.Start_Line(account_pack={"account": "dennisliuu@gmail.com", "password": 'bid440edit839', "fallback": ""})
        if login_stat == None:
            print("登入失敗")
        pass




if __name__ == '__main__':
    obj = Main()
    # obj.Start()
