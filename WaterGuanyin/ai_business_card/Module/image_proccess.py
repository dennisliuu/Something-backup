# -*- coding: utf-8 -*-

from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
import requests


class ImageProccess:
    def __init__(self, font_size=120, font_color=(255, 255, 255)):
        self.font = ImageFont.truetype("../font/msjhbd.ttc", font_size)
        self.font_color = font_color
        self.workstat_list = ['前鎮就業服務站@高雄市前鎮區鎮中路6號1樓@07-8220790', '左營就業服務站@高雄市左營區忠言路189號1樓@07-5509848', '三民就業服務站@高雄市三民區大順二路468號10樓@07-3837191', '楠梓就業服務站@高雄市楠梓區學專路777號2樓@07-3609521', '鳳山就業服務站@高雄市鳳山區中山西路235號@07-7410243', '岡山就業服務站@高雄市岡山區民有路27號@07-6228321', '楠梓就業服務台@高雄市楠梓區經二路15號1樓@07-3640508', '前鎮就業服務台@高雄市前鎮區高雄加工區中六路與環區一路口@07-8418227', '鳥松就業服務台@高雄市鳥松區大埤路117號1樓@07-7331824', '仁武就業服務台@高雄市仁武區工業二路3號@07-3749554', '大寮就業服務台@高捷OT1大寮站2號出口2樓店面，高雄市大寮區捷西路300號(郵寄地址)@07-7825009', '燕巢就業服務台@高雄市燕巢區中安路1號@07-6162801', '路竹就業服務台@高雄市路竹區國昌路76號@07-6071047', '旗山就業服務台@高雄市旗山區延平一路495號2樓@07-6623656', '永安就業服務台@高雄市永安區永工二路1號@07-6245031', '本洲就業服務台@高雄市岡山區本工路17號@07-6246155', '旗津就業服務台@高雄市旗津區旗津三路2號@07-5714116', '林園就業服務台@高雄市林園區王公路1號1樓@07-6466185', '大社就業服務台@高雄市大社區大社里自強街1號@07-3539044', '大樹就業服務台@高雄市大樹區龍目路158號2樓@07-6529406', '美濃就業服務台@高雄市美濃區合和里美中路260號@07-6820711', '六龜就業服務台@高雄市六龜區民治路18號@07-6892488', '甲仙就業服務台@高雄市甲仙區和安里中山路50號@07-6751744', '桃源就業服務台@高雄市桃源區桃源里北進巷1號@07-6861336', '茂林就業服務台@高雄市茂林區茂林里8-3號@07-6801385', '那瑪夏就業服務台@高雄市那瑪夏區大光巷230號@07-6701275', '梓官就業服務台@高雄市梓官區梓官路258號@07-6194849', '阿蓮就業服務台@高雄市阿蓮區民生路94號@07-6315428', '湖內就業服務台@高雄市湖內區中正路二段77號@07-6992271', '茄萣就業服務台@高雄市茄萣區濱海路四段27號@07-6909738', '橋頭就業服務台@高雄市橋頭區隆豐路1號@07-6126883', '彌陀就業服務台@高雄市彌陀區彌仁里中華路4號@07-6194850', '內門就業服務台@高雄市內門區內門里內門20號@07-6674851', '杉林就業服務台@高雄市杉林區上平里山仙路6號@07-6774420']
    def get_image(self, keyword, image,need_text=0):
        if type(image) == str:
            response = requests.get(image)
            img = Image.open(BytesIO(response.content))
        else:
            img = image
        if len(img.split()) == 4:
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))

        index = 0
        if len(keyword) == 3:
            image_size = (2500, 843)
            img = img.resize(image_size, Image.ANTIALIAS)
            draw = ImageDraw.Draw(img)
            if need_text == 1:
                for i in range(0, 2499, 833):
                    text_size = draw.textsize(str(keyword[index]), self.font)
                    text_position = ((image_size[0] - text_size[0]) // 2 + i - image_size[0] // 3,
                                     (image_size[1] - text_size[1]) // 2)
                    draw.text(text_position, str(
                        keyword[index]), tuple(self.font_color), font=self.font)
                    index += 1
        elif len(keyword) == 6:
            image_size = (2500, 1686)
            img = img.resize(image_size, Image.ANTIALIAS)
            draw = ImageDraw.Draw(img)
            if need_text == 1:
                for i in range(0, 1686, 843):
                    for j in range(0, 2499, 833):
                        text_size = draw.textsize(
                            str(keyword[index]), self.font)
                        text_position = ((image_size[0] - text_size[0]) // 2 + j - image_size[0] // 3,
                                         (image_size[1] - text_size[1]) // 2 + i - image_size[1] // 4)
                        draw.text(text_position, str(
                            keyword[index]), tuple(self.font_color), font=self.font)
                        index += 1
        else:
            return
        output = BytesIO()
        try:
            img = img.convert('RGB')
        except:
            pass
        img.save("tmp.jpg")

if __name__ == "__main__":
    obj = ImageProccess()
    obj.Cover_Image()