import time
import json
import requests
import os
import pprint
from threading import Thread
from urllib import parse
from flask import Flask, request, render_template, url_for, redirect
from flask_cors import CORS
from Controller import Line_Bot_Controller
from Module import image_proccess
from Module import line
from pprint import pprint
from datetime import datetime
from PIL import ImageFont
import jin
from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
    TemplateSendMessage, CarouselTemplate, CarouselColumn, BoxComponent,
    BubbleContainer, ButtonsTemplate, PostbackTemplateAction,
    MessageTemplateAction, URITemplateAction, FlexSendMessage, MessageEvent,
    TextMessage, TextSendMessage, SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction, ButtonsTemplate,
    ImageCarouselTemplate, ImageCarouselColumn, URIAction, PostbackAction,
    DatetimePickerAction, CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent, StickerMessage,
    StickerSendMessage, LocationMessage, LocationSendMessage, ImageMessage,
    VideoMessage, AudioMessage, FileMessage, UnfollowEvent, FollowEvent,
    JoinEvent, LeaveEvent, BeaconEvent, FlexSendMessage, BubbleContainer,
    ImageComponent, BoxComponent, TextComponent, SpacerComponent,
    IconComponent, ButtonComponent, SeparatorComponent, QuickReply,
    QuickReplyButton)
import socket
import importlib.util
import socket

Debug_Mode = False

app = Flask(__name__, template_folder="templates")
app.jinja_env.variable_start_string = '[['
app.jinja_env.variable_end_string = ']]'
CORS(app)


# Jin_API.listen_web_get_news_return
class Aichatin_Line():
    def __init__(self):
        self.Config = Config()
        self.Line_Bot_API = LineBotApi(self.Config.LINE_TOKEN)
        self.Line_Controller = Line_Bot_Controller.Line_Controller(
            LARAVEL_HOST=None, line_bot_api=self.Line_Bot_API)

    def Init_Menu(self):
        self.Line_Controller.Delete_All_Menu()
        keywords = [{
            'loc': [0, 0, 378, 425],
            'msg': "FoodPanda"
        }, {
            'loc': [375, 0, 467, 425],
            'msg':
            '立即叫車',
            'callback':
            URIAction(label='立刻叫車', uri='line://app/1653562515-2OjoQORx')
        }, {
            'loc': [839, 0, 362, 422],
            'msg':
            "全球訂房",
            'callback':
            URIAction(label='立刻叫車', uri='line://app/1653562515-Aqa9Mg1r')
        }, {
            'loc': [841, 431, 357, 391],
            'msg':
            "聯絡小誠",
            'callback':
            URIAction(label='立刻叫車', uri='line://app/1653562515-8x4n6DbQ')
        }, {
            'loc': [0, 431, 378, 391],
            'msg': '財金資訊訂閱'
        }, {
            'loc': [383, 431, 500, 391],
            'msg': "即時新聞"
        }]
        img = open("./asset/richmenu2.png", 'rb')
        menu_hash = self.Line_Controller.Add_Richmenu(keywords, img_url=img)
        self.Line_Bot_API.set_default_rich_menu(menu_hash)


class Config:
    def __init__(self):
        # self.LINE_TOKEN = "hmWAmjWQ8Y6UWC7kzvdYAXLNOuzxrF61IQa7d4zol7zg5YQxeblzoXnQOivYutnX3ZBALrZLwGSOnpVajBW6jXknO/v56yJjBBUfcGs5ncnHjQ/dbsesXhoBH3YAU7Q5iA3NEu1oYvR3/iR2KUE/nQdB04t89/1O/w1cDnyilFU="
        self.LINE_TOKEN = "qObchsEFcHifMFb/jgeEdQn/Kk/C+21vElcHacYRYVxypRGH0uGCKHybz7qsVCdOwJL6wwB0rLHl5Jb7Ys4oWwmAnNHHsibDATLobVPAtEBwyCEd9JxkHxzqB6eek8LBPWIW8rspGmoB6VepFFV7DAdB04t89/1O/w1cDnyilFU="
        # self.LINE_SECRET = "c5380c5bd441f87500a37e6f4df51a79"
        self.LINE_SECRET = "76161ce6faa33e4bffbf7ee9ec3c706b"
        self.online = False
        self.LARAVEL_HOST = "127.0.0.1"

    # def get(self):
    #     rs = requests.get("{}/api/config".format(self.LARAVEL_HOST))
    #     try:
    #         self.LINE_TOKEN = rs.json()["token"]
    #     except Exception as e:
    #         print(e)
    #         self.LINE_TOKEN = "HBxoJxAIXURh0S+vWHZRIdVbmNIjlVD7xklF8m8oRmZIMLRyBsMH7IyFNdZ7bPmZ0Zt0z563F808Q8KvD0+syYlTuhYfJRBmHKHhD1g2UyoNLU/Tv6aFXLtrdrxa8QLl3uGhcMl+g2IBESQZbUMCtwdB04t89/1O/w1cDnyilFU="
    #     try:
    #         self.LINE_SECRET = rs.json()["secret"]
    #     except Exception as e:
    #         print(e)
    #         self.LINE_SECRET = "a991717709be12606ab57a29e8f86ff8"


Config_obj = Config()
Line_Bot_OBJ = LineBotApi(Config_obj.LINE_TOKEN)

from Controller import Message_Controler
Msg_Controller = Message_Controler.Message_Controller(Line_Bot_OBJ)


@app.route('/search', methods=['GET', 'POST'])
def search():
    user_id = request.args.get('user_id')
    if request.method == 'GET':
        return '<form action="/search" method="post"> Question: <input type="text" name="message" /><input type="text" style="display:none" name="user_id" value={} /> <input type="submit" value="Submit"> </form>'.format(user_id)
    if request.method == 'POST':
        user_id = request.values['user_id']
        print(user_id)
        message = "你的問題：" + request.values['message'] + "，我不回答"
        Line_Bot_OBJ.push_message(user_id, TextMessage(type='text', text=message))
        return '<h1>Question submit success!</h1>'

@app.route("/", methods=['POST', 'GET'])
def line_webhook():
    global Msg_Controller

    try:
        body = request.get_data(as_text=True)
        print("body----------------------")
        print("----------------------------------------------------")
        print(body)
        print("----------------------------------------------------")

        data = json.loads(body)
    except:
        return "ok"
    # print(data['events'])

    event = data['events'][0]
    print(event)
    if event['type'] == "message":

        Msg_Controller.Msg_Response(event)

    if event['type'] == "follow":

        rb = CarouselColumn(
            thumbnail_image_url="https://i.imgur.com/6cILT61.png",
            title="您好!我是小誠",
            text="請參考我的簡歷",
            actions=[
                URIAction(
                    label='點擊前往',
                    uri=
                    'http://frenify.com/envato/marketify/html/arlo/1/index-2.html'
                ),
            ])
        carousel_template = CarouselTemplate(columns=[rb])

        # tb = TemplateSendMessage(alt_text="相關訊息", template=carousel_template)
        tb = ImageSendMessage("https://i.imgur.com/6cILT61.png",
                              "https://i.imgur.com/6cILT61.png")
        Line_Bot_OBJ.reply_message(event['replyToken'], tb)

    return 'OK'


if __name__ == "__main__":
    obj = Aichatin_Line()
    # obj.Init_Menu()
    app.run(
        '0.0.0.0',
        debug=True,
        port=1188,
        use_reloader=False,
        # ssl_context=("/etc/letsencrypt/live/asurada.testcat.ga-0001/fullchain.pem","/etc/letsencrypt/live/asurada.testcat.ga-0001/privkey.pem")
    )
