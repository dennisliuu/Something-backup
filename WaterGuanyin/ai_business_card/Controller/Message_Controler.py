import os
import random
import json
from Module import net_fn
import dateutil.parser
import requests
from linebot.models import (

    ImagemapSendMessage,BaseSize,ImagemapArea,URIImagemapAction,MessageImagemapAction,
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn,
    BoxComponent, VideoSendMessage,
    BubbleContainer, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction, FlexSendMessage,
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton
)
from linebot import (
    LineBotApi, WebhookHandler
)
from Module import fd,hotels
import jin
from threading import Thread
from Module import YahooFeed
class Message_Controller():
    def __init__(self, line_bot_api):
        self.LARAVEL_HOST = "127.0.0.1"
        self.line_bot_api = line_bot_api  # type: LineBotApi
        self.Net = net_fn.Net()
        self.QA_Table = {}
        self.Hotels = hotels.Hotels()
        self.Yahoofeed = YahooFeed.YahooFeed()
        # self.Load_QATable()

        Jin_API = jin.Jin()
        Jin_API.init_news()
        t = Thread(target=Jin_API.listen_web_get_news_return)
        t.start()
        self.Jin_API = Jin_API

    def Load_QATable(self):
        path = "./asset/wash_data.csv"
        if os.path.exists(path) == False:
            path = ".{}".format(path)
        end = {}
        with open(path, "r",encoding="utf-8") as f:
            data = f.read()
            data= data.split("\n")
            for r in data:

                rows = r.split(",")
                if len(rows)!= 3:
                    continue
                pack = {'cat':rows[0],'name':rows[1],'connect':rows[2]}
                cat = pack['cat']
                if pack['name'] == "":
                    continue
                if cat not in end:
                    end[cat] = []
                end[cat].append(pack)
                # print(pack)
            # print(data)
        self.QA_Table = end
        # print(len(self.QA_Table))
    def Msg_Response(self,event):
        source_type = event["source"]["type"]
        # 判別對象為群組或是個人
        print(event)
        if source_type == "user":
            user_id = event["source"]["userId"]
            if event['message']['type'] == "text":
                txt_data = event['message']['text']
                if txt_data == "我的手機：0988655777":
                    tb = ImageSendMessage("https://i.imgur.com/6cILT61.png", "https://i.imgur.com/6cILT61.png")
                    self.line_bot_api.reply_message(event['replyToken'], tb)


                if txt_data == "財金資訊訂閱":
                    box_list = []
                    for new in self.Jin_API.news:

                        new_msg = self.Jin_API.news[new].replace("<b>","").replace("</b>","").replace("<br/>","")
                        if "</a>" in new_msg:
                            continue
                        work_time = dateutil.parser.parse(new)
                        line_msg = "{}  \n於{}".format(new_msg,work_time)
                        box_list.append(line_msg)
                    box_list = box_list[-3:]
                    msg = "\n----\n----\n".join(box_list)
                    self.line_bot_api.reply_message(
                        event["replyToken"], TextMessage(type='text',text=msg))
                if txt_data == "立即叫車":
                    buttons_template = ButtonsTemplate(
                        title='叫車服務', text='歡迎使用叫車服務，本服務由大都會計程車進行技術支援', actions=[
                            URIAction(label='立刻叫車', uri='line://app/1653562515-2OjoQORx'),
                        ])
                    template_message = TemplateSendMessage(
                        alt_text='Buttons alt text', template=buttons_template)
                    self.line_bot_api.reply_message(event["replyToken"], template_message)

                if txt_data == "即時新聞":
                    self.line_bot_api.reply_message(event["replyToken"], TextMessage(label='aaa',text="讀取中..."))

                    feed = self.Yahoofeed
                    feed.get_feedinfo()
                    feed.get_postcontext()
                    data = feed.pack_together()
                    n_list = []
                    for zc, fc in enumerate(data):
                        # print(fc)
                        if zc > 8:
                            break
                        if fc['picture'] == "":
                            continue
                        rb = CarouselColumn(
                            thumbnail_image_url=fc['picture'].replace("http://","https://"),
                            title=fc['title'][:30]+"...",
                            text=fc['context'][:55]+"...",
                            actions=[URIAction(uri=fc['link'], label='點擊閱讀')]
                        )
                        # print(fc['context'][:10])
                        print(fc['picture'])
                        n_list.append(rb)
                    carousel_template = CarouselTemplate(
                        columns=n_list
                    )
                    self.line_bot_api.push_message(
                        event["source"]['userId'],
                        TemplateSendMessage(alt_text="即時熱點新聞", template=carousel_template))

                if txt_data == "FoodPanda":
                    self.line_bot_api.reply_message(
                        event["replyToken"], TextMessage(type='text', text="系統記錄您的地址為：\n【台北市中正區漢口街一段45號8樓】\n，開始為您搜索附近..."))
                    food_panda_list = fd.FoodPanda('台北市中正區漢口街一段45號8樓').fetch_all_restaurants()
                    food_panda_list = json.loads(food_panda_list)
                    n_list = []
                    for zc,fc in enumerate(food_panda_list):
                        # print(fc)
                        if zc >8:
                            break
                        rb = CarouselColumn(
                            thumbnail_image_url=fc['img'],
                            title=fc['name'],
                            text="營業中",
                            actions= [ URIAction(  uri=fc['url'],  label='點餐')]
                        )
                        n_list.append(rb)
                    carousel_template = CarouselTemplate(
                        columns=n_list
                    )
                    self.line_bot_api.push_message(
                        event["source"]['userId'], TemplateSendMessage(alt_text="附近前十大熱門餐廳", template=carousel_template))
                else:
                    # LIFF
                    seach_url = 'line://app/1653631284-b0OLvQXv?' + 'user_id=' + event["source"]['userId'] +'&&'+ 'message=' + txt_data
                    print(seach_url)
                    buttons_template = ButtonsTemplate(
                        title='直接回覆', text='歡迎直接詢問', actions=[
                            URIAction(label='直接回覆', uri=seach_url),
                        ])
                    template_message = TemplateSendMessage(
                        alt_text='Buttons alt text', template=buttons_template)
                    self.line_bot_api.reply_message(event["replyToken"], template_message)

    def Unlink_Richmenu_All_User(self):
        url = "{}/api/line_users".format(self.LARAVEL_HOST)
        rs = self.Net.Get(url)
        datas = json.loads(rs.text)
        users = []
        for item in datas['data']:
            users.append(item['user_id'])
        print(users)
        self.line_bot_api.unlink_rich_menu_from_users(users)

    def Line_Fall_Back(self, event, txt_data):
        response_chk = self.Check_Has_Keyword_Response(txt_data)
        # 確認是不是有符合的模糊關鍵字
        response_type = "text"
        if response_chk != False:
            Fall_Back_Item = response_chk
            # Reply_Message = response_chk['response']
            # response_type = response_chk['ele_type']
        else:
            Fall_Back_Item = self.Get_Fall_Back()
        # print("replay:{}")
        # print(Fall_Back_Item)

        # 發送訊息
        # if response_type == "text" or response_type == "phone":
        #     self.line_bot_api.reply_message(
        #         event["replyToken"], TextSendMessage(text=Reply_Message))
        # if response_type == "image":
        #     Reply_Message = "{}{}".format(self.LARAVEL_HOST,Reply_Message)
        #     # print(Reply_Message)
        #     self.line_bot_api.reply_message(
        #         event["replyToken"], ImageSendMessage(Reply_Message,Reply_Message))
        # if response_type == "video":
        #     Reply_Message = "{}{}".format(self.LARAVEL_HOST,Reply_Message)
        #     # print(Reply_Message)
        #     self.line_bot_api.reply_message(
        #         event["replyToken"], VideoSendMessage(Reply_Message,"{}/images/logo.png".format(self.LARAVEL_HOST)))
        print("event:{}".format(event))
        self.Send_Msg_Step(Fall_Back_Item, event['source']["userId"], txt_data)

        return True
    # 按順序發送訊息

    def Send_Msg_Step(self, back_item, Token, message):
        try:
            json_work = json.loads(back_item['work_json'])
        except json.decoder.JSONDecodeError:
            json_work = []
        test_json = {
            "type": "image-mod",
            "data": {
                "ratio": "none",
                "pack": [
                    {
                        "img": "https://24eshop.testcat.ga/images/1568949332.png",
                        "title": "早安",
                        "description": "痾",
                        "url": "http://www.macc.com.tw/page/4",
                        "buttons": [
                            {
                                "text": "前往網站",
                                "type": "url",
                                "data": "http://www.macc.com.tw/page/4"
                            }
                        ]
                    },
                    {
                        "img": "https://24eshop.testcat.ga/images/1568949332.png",
                        "title": "美之城",
                        "description": "要好好吃早餐",
                        "url": "http://www.macc.com.tw/page/4",
                        "buttons": [
                            {
                                "text": "網站網站",
                                "type": "postback",
                                "data": "aaa"
                            }
                        ]
                    }
                ]
            }
        }
        # json_work.append(test_json)
        print("----------------------")
        for item in json_work:
            if item['type'] == "text":
                self.line_bot_api.push_message(
                    Token, TextSendMessage(text=item["data"]))
            if item['type'] == "image":
                img_url = "{}{}".format(self.LARAVEL_HOST, item['url'])
                print(img_url)
                self.line_bot_api.push_message(
                    Token, ImageSendMessage(img_url, img_url))

            if item['type'] == "video":
                video_url = "{}{}".format(self.LARAVEL_HOST, item['url'])
                # print(img_url)
                self.line_bot_api.push_message(
                    Token, VideoSendMessage(video_url, "{}/images/logo.png".format(self.LARAVEL_HOST)))

            if item['type'] == 'image-mod':
                data = item['data']
                ratio = data['ratio']
                pack = data['pack']
                self.send_carousel_template(pack, Token, message)

        # print(json_work)

        pass

    def Check_Has_Keyword_Response(self, word):
        rs = requests.get("{}/api/keyword_resp".format(self.LARAVEL_HOST))
        # print("---------------------")
        # print(rs.text)
        keywords = json.loads(rs.text)['data']
        for rsp_item in keywords:
            keyword = rsp_item["keyword"]
            if keyword in word:
                # print(rsp_item)
                return rsp_item
        return False

    def Get_Fall_Back(self):
        rs = requests.get("{}/api/keyword_resp".format(self.LARAVEL_HOST))
        # print("---------------------")
        # print(rs.text)
        keywords = json.loads(rs.text)['data']
        for rsp_item in keywords:
            keyword = rsp_item["keyword"]
            if "例外訊息" in keyword:
                # print(rsp_item)
                return rsp_item
        return False

    def Switch_Menu(self, Token_id, menu_db_id):
        menu_list = self.Get_Tab_List()
        menu_db_id = menu_db_id.replace("tab:", "")
        try:
            menu_db_id = int(menu_db_id)
        except Exception as e:
            print("menu_db_id error")
            print(e)
            return False
        for item in menu_list:
            if item['id'] == menu_db_id:
                self.line_bot_api.link_rich_menu_to_user(
                    user_id=Token_id, rich_menu_id=item['menuhash'], timeout=None)

    def Get_Tab_List(self):
        url = "{}/api/menu_list".format(self.LARAVEL_HOST)
        # print(url)
        rs = self.Net.Get(url=url)
        txt = rs.text
        menu_list = json.loads(txt)
        return menu_list

    def send_carousel_template(self, pack, receiver_id, message):
        item_msg_cols = []
        for i, item in enumerate(pack):
            img = item['img']
            if "https://" not in img:
                img = item['img'].replace("http", "https")
            print(img)
            url = item['url']
            if "https://" not in url:
                url = item['url'].replace("http", "https")
            actions = []
            # 處理按鍵
            for button in item['buttons']:
                action = None
                if button['type'] == "url":
                    if "https://" not in button['data']:
                        button['data'].replace("http", "https")
                    action = URITemplateAction(
                        label=button['text'],
                        uri=button['data']
                    )
                elif button['type'] == "postback":
                    action = PostbackTemplateAction(
                        label=button['text'],
                        data=button['data']
                    )
                if action:
                    actions.append(action)
            carousel_column = CarouselColumn(
                thumbnail_image_url=img,
                title=item['title'],
                text=item['description'],
                actions=actions
            )
            item_msg_cols.append(carousel_column)

        carousel_template = CarouselTemplate(
            columns=item_msg_cols
        )
        self.line_bot_api.push_message(
            receiver_id, TemplateSendMessage(alt_text=message, template=carousel_template))

    def order_response(self, user_id, title, price, img, quantity, orderUrl):
        if "https://" not in orderUrl:
            orderUrl.replace("http", "https")
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url=img,
                size='full',
                aspect_ratio='17:13',
                aspect_mode='cover',
                action=URIAction(
                      uri=img,
                      label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text=title,
                                  weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(
                                size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(
                                size='sm', url='https://example.com/grey_star.png'),
                            IconComponent(
                                size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(
                                size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(
                                size='sm', url='https://example.com/grey_star.png'),
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='價格',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text=price,
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='數量',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text=quantity,
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    SpacerComponent(size='sm'),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URITemplateAction(
                            uri=orderUrl, label='立即付款'),
                    ),
                ]
            ),
        )
        message = FlexSendMessage(alt_text="這是您的購物訊息", contents=bubble)
        self.line_bot_api.push_message(
            user_id, message
        )


if __name__ == "__main__":

    obj = Message_Controller("http://127.0.0.1:8000")
    # obj.Get_Tab_List()
    print(obj)
    obj.Load_QATable()