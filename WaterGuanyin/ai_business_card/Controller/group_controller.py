import json
import requests
from Module import net_fn
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
    SeparatorComponent, QuickReply, QuickReplyButton
)
from linebot import (
    LineBotApi, WebhookHandler
)


class GroupController:
    def __init__(self, LARAVEL_HOST, bot, message_controller):
        self.LARAVEL_HOST = LARAVEL_HOST
        self.bot = bot
        self.Net = net_fn.Net()
        self.message_controller = message_controller

    def join_group_handler(self, group_id):
        rs = self.Net.Poster(
            "{}/api/group/{}".format(self.LARAVEL_HOST, group_id), data={"status": 1})
        pass

    def leave_group_handler(self, group_id):
        rs = self.Net.Poster(
            "{}/api/group/{}".format(self.LARAVEL_HOST, group_id), data={"status": 0})
        pass

    def message_handler(self, message, group_id):
        is_replied = False
        # 驗證關鍵字
        rs = requests.get("{}/api/keywords".format(self.LARAVEL_HOST))
        keywords = json.loads(rs.text)["data"]
        for keyword in keywords:
            if (message == keyword["word"]):
                goods = json.loads(keyword["goods"])
                good_list = []
                for good in goods:
                    rs = requests.get(
                        "{}/api/goods/{}".format(self.LARAVEL_HOST, good))
                    goodInfo = json.loads(rs.text)["data"]
                    good_list.append(goodInfo)
                item_msg_cols = []
                for i, good in enumerate(good_list):
                    img = good['img'].replace("http", "https")
                    rb = CarouselColumn(
                        thumbnail_image_url=img,
                        title=good['title'],
                        text="售價"+str(good['price'])+"元",
                        actions=[
                            URITemplateAction(
                                label='前往網站',
                                uri=good['link']
                            ),
                        ]
                    )
                    item_msg_cols.append(rb)
                carousel_template = CarouselTemplate(
                    columns=item_msg_cols
                )
                Reply_Message = "以下為 {} 的商品".format(message)
                self.bot.push_message(
                    group_id, TextSendMessage(text=Reply_Message))
                self.bot.push_message(
                    group_id, TemplateSendMessage(alt_text=message, template=carousel_template))
                is_replied = True
        if not is_replied:
            try:
                # 確認是不是有符合的模糊關鍵字
                response_chk = self.message_controller.Check_Has_Keyword_Response(
                    message)
                response_type = "text"
                if response_chk != False:
                    fall_back_item = response_chk
                else:
                    fall_back_item = self.message_controller.Get_Fall_Back()
                self.message_controller.Send_Msg_Step(
                    fall_back_item, group_id, message)
            except:
                pass
