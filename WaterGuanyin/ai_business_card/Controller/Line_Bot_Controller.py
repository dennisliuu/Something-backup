import json
from Module import net_fn
import requests
from Module import YahooFeed
from linebot.models import (
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
    SeparatorComponent, QuickReply, QuickReplyButton, ImagemapSendMessage, BaseSize, MessageImagemapAction, ImagemapArea,RichMenu,RichMenuArea,RichMenuSize,RichMenuBounds
)
from linebot import (
    LineBotApi, WebhookHandler
)
import os

from Module import image_proccess
import os

class Line_Controller():
    def __init__(self, LARAVEL_HOST, line_bot_api):
        self.LARAVEL_HOST = LARAVEL_HOST

        self.line_bot_api = line_bot_api  # type: LineBotApi
        # print(self.line_bot_api.__dict__)
        self.Line_Token = self.line_bot_api.headers["Authorization"]
        self.Line_Token = self.Line_Token.replace("Bearer ", "")
        # self.proxy_ip = "127.0.0.1:6666"
        self.proxy_ip = None
        print("token:{}".format(self.Line_Token))
        self.Net = net_fn.Net()


    def Delete_All_Menu(self):
        menu_list = self.line_bot_api.get_rich_menu_list()
        for menu in menu_list:
            # print(menu.__dict__)
            dmenu = menu.__dict__
            # print(json.dumps(dmenu,default=str))
            menu_id = dmenu['rich_menu_id']
            self.line_bot_api.delete_rich_menu(menu_id)

    def Reload_All_Richmenu(self):
        self.Delete_All_Menu()
        menu_list = self.Get_All_Server_Menu()
        default_menu_hash = None
        for menu in menu_list:
            keyword = menu['keywords']
            keyword = json.loads(keyword)
            imageUrl = self.LARAVEL_HOST + menu['image']
            try:
                menuhash = self.Add_Richmenu(keyword, imageUrl)
                # print(menuhash)
                self.Upload_Menu_To_Server(menu['id'], menuhash)
                if menu['is_default'] == 1:
                    self.line_bot_api.set_default_rich_menu(menuhash)
                    default_menu_hash = menuhash
            except:
                pass
        return default_menu_hash

    def Get_All_Server_Menu(self):
        url = "{}/api/menu_list".format(self.LARAVEL_HOST)
        rs = self.Net.Get(url)
        data = None
        try:
            data = rs.text
            data = json.loads(data)
            # return data
        except Exception as e:
            print(e)
        return data

    def Upload_Menu_To_Server(self, menu_id, line_hash):
        data = {"id": menu_id, "menuhash": line_hash}

        url = "{}/api/update_menuhash".format(self.LARAVEL_HOST)
        rs = self.Net.Poster(url, data, proxy_ip=self.proxy_ip)
        # print(rs.text)

    def set_default_menu(self, user_id):
        menus = self.Get_All_Server_Menu()
        default_menu = None
        for menu in menus:
            if menu["is_default"] == 1:
                default_menu = menu["menuhash"]
                break
        if default_menu:
            self.switch_menu_by_id(user_id, default_menu)
            # print(default_menu)

    def switch_menu_by_id(self, user_id, menu_id):
        self.line_bot_api.link_rich_menu_to_user(user_id, menu_id)

    def send_num_imagemap(self, user_id):
        base_url = "{}/api/num-image".format(self.LARAVEL_HOST)
        base_url = "{}/api/num-image".format("https://f8b5f6cd.ngrok.io")
        imagemap_message = ImagemapSendMessage(
            base_url=base_url,
            alt_text='數字鍵盤',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                MessageImagemapAction(
                    text='1',
                    area=ImagemapArea(
                        x=0, y=0, width=347, height=260
                    )
                ),
                MessageImagemapAction(
                    text='2',
                    area=ImagemapArea(
                        x=347, y=0, width=347, height=260
                    )
                ),
                MessageImagemapAction(
                    text='2',
                    area=ImagemapArea(
                        x=694, y=0, width=346, height=260
                    )
                ),
                MessageImagemapAction(
                    text='4',
                    area=ImagemapArea(
                        x=0, y=260, width=347, height=260
                    )
                ),
                MessageImagemapAction(
                    text='5',
                    area=ImagemapArea(
                        x=347, y=260, width=347, height=260
                    )
                ),
                MessageImagemapAction(
                    text='6',
                    area=ImagemapArea(
                        x=694, y=260, width=346, height=260
                    )
                ),
                MessageImagemapAction(
                    text='7',
                    area=ImagemapArea(
                        x=0, y=520, width=347, height=260
                    )
                ),
                MessageImagemapAction(
                    text='8',
                    area=ImagemapArea(
                        x=347, y=520, width=347, height=260
                    )
                ),
                MessageImagemapAction(
                    text='9',
                    area=ImagemapArea(
                        x=694, y=520, width=346, height=260
                    )
                ),
                MessageImagemapAction(
                    text='10',
                    area=ImagemapArea(
                        x=0, y=780, width=1040, height=260
                    )
                ),
            ]
        )
        self.line_bot_api.push_message(user_id, imagemap_message)

    def switch_to_num_richmenu(self, user_id):
        area = []
        index = 0
        for i in range(0, 1686, 843):
            for j in range(0, 2499, 833):
                if index >= 5:
                    break
                template = {
                    "bounds": {
                        "x": j,
                        "y": i,
                        "width": 833,
                        "height": 843
                    }
                }
                action_pack = {"type": "postback",
                               "label": str(index + 1),
                               "data": "action=order&quantity={}".format(index + 1)}
                template["action"] = action_pack
                area.append(template)
                index += 1
        payload = {
            "size": {
                "width": 2500,
                "height": 1686
            },
            "selected": "true",
            "name": "richmenu-six",
            "chatBarText": "選擇數量",
            "areas": area
        }
        headers = {
            "Authorization": "Bearer {}".format(self.Line_Token),
            "Content-Type": "application/json"
        }
        rs = requests.post("https://api.line.me/v2/bot/richmenu",
                           data=json.dumps(payload), headers=headers, verify=False)
        menu_id = rs.json()["richMenuId"]
        try:
            sample_img = "{}\data\\num.png".format(os.getcwd())
            print(sample_img)
            with open(sample_img, 'rb') as f:
                self.line_bot_api.set_rich_menu_image(menu_id, "image/png", f)
        except FileNotFoundError:
            print("file_stat:{}".format(os.path.isfile("./data/num.png")))
            print(os.getcwd())
            print("img_file_upload_number error")
            pass

        rs = requests.post(
            "https://api.line.me/v2/bot/user/{}/richmenu/{}".format(user_id, menu_id), headers=headers)
        print("num_:{}".format(rs.text))
        return menu_id
        # rs = requests.post(
        #     "https://api.line.me/v2/bot/user/all/richmenu/{}".format(menu_id), headers=headers)
        # print(rs.text)

    def get_menu_from_user(self, user_id):
        return self.line_bot_api.get_rich_menu_id_of_user(user_id)

    def Add_Richmenu(self, keyword, img_url=None):
        if img_url == str:
            processor = image_proccess.ImageProccess()
            processor.get_image(keyword, img_url)
        else:
            processor = img_url

        # print(type(keyword))
        area = []
        index = 0
        height = 810
        for key in keyword:
            loc = key['loc']

            action_pack = MessageAction(label=key['msg'],text=key['msg'])
            if 'callback' in key:
                action_pack = key['callback']

            # template["action"] = action_pack
            area.append(RichMenuArea(
                bounds=RichMenuBounds(x=loc[0], y=loc[1], width=loc[2], height=loc[3]),
                action=action_pack))
            # area.append(template)
            index += 1

        rich_menu_to_create = RichMenu(
            size=RichMenuSize(width=1200, height=810),
            selected=False,
            name="Nice richmenu",
            chat_bar_text="打開選單",
            areas=area
        )

        # print(rich_menu_to_create)
        menuId =  self.line_bot_api.create_rich_menu(
        rich_menu=rich_menu_to_create)
        print(menuId)
        if type(img_url) == str:
            try:
                with open("./tmp.jpg", 'rb') as f:
                    self.line_bot_api.set_rich_menu_image(menuId, "image/jpeg", f)
            except FileNotFoundError:
                pass
            try:
                os.remove("./tmp.jpg")
            except OSError as e:
                print(e)
        else:
            self.line_bot_api.set_rich_menu_image(menuId, "image/jpeg", img_url)
        return menuId

        # pass
if __name__ == "__main__":
    line_bot_api = LineBotApi(
        "9gYV7IeC2d+3EFkDx8lnZwg97Z6N00HwwXYQyxv9FumFjaa6yT3tDIFys6Wp7THvIKILX/aJ1tRbAOz3IDSzocuKBOeMpqS0m43G0L5KFNnWb6r1F8DCOGX3wdnKrXRd2sZBoAp398jlofUba6zALwdB04t89/1O/w1cDnyilFU=")
    obj = Line_Controller("http://127.0.0.1:8000", line_bot_api)
    obj.Reload_All_Richmenu()
    # obj.Get_Tab_List()
    # obj.Reload_All_Richmenu()
