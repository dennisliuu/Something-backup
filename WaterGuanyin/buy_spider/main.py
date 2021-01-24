import json
from flask import Flask, render_template, request

# from Module.mpglobal_ja import PythonJa
# from Module.hasegawasaketen import Hasegawa
# from Module.uniqlo import Uniqlo
# from Module.biccamera import Biccamera
# from Module.onitsukatiger import OnitsukaTiger
# from Module.coach import Coach
# from Module.Lego import Lego
# from Module.nike import Nike
# from Module.Tiffany import Tiffany

from craw_module.mpglobal_ja import PythonJa
from craw_module.hasegawasaketen import Hasegawa
from craw_module.uniqlo import Uniqlo
from craw_module.biccamera import Biccamera
from craw_module.onitsukatiger import OnitsukaTiger
from craw_module.coach import Coach
from craw_module.Lego import Lego
from craw_module.Tiffany import Tiffany
from craw_module.nike import Nike


app = Flask(__name__, template_folder="templates")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get-page-info', methods=['POST'])
def get_page_info():
    rs = request.form
    item_url = rs['item_url']
    source = None
    rqs = None
    if item_url.find('https://mpglobal.donki.com') != -1:
        source = PythonJa()
    elif item_url.find('https://www.hasegawasaketen.com') != -1:
        source = Hasegawa()
    elif item_url.find('https://www.uniqlo.com/') != -1:
        source = Uniqlo()
    elif item_url.find('https://www.biccamera.com/') != -1:
        source = Biccamera()
    elif item_url.find('https://www.onitsukatigermagazine.com/') != -1:
        source = OnitsukaTiger()#title error
    elif item_url.find('https://www.coach.com') != -1:
        source = Coach()
    elif item_url.find("https://www.lego.com") != -1:
        source = Lego()
    elif item_url.find("https://www.nike.com") != -1:
        source = Nike()
    elif item_url.find('https://www.tiffany.com/') != -1:
        source = Tiffany()

    if source:
        rqs = source.get_single_page(item_url)
        if "price_jp" in rqs:
            rqs['price'] = rqs['price_jp']
        if "other_image" in rqs:
            rqs['other_image'] = rqs['other_image'].replace('\n',"")
        if "main_image" not in rqs:
            if type(rqs['main_images']) != list:
                rqs['main_image'] = rqs['main_images']
            else:
                rqs['main_image'] = rqs['main_images'][0]
        if "description" not in rqs and "spec" in rqs:
            rqs['description'] = rqs['spec']['main']
    if rqs:
        return render_template('item_info.html', item_info=json.dumps(rqs, ensure_ascii=False))
    else:
        return render_template('index.html', error='錯誤的商品網址！')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8999", debug=True, use_reloader=False)
