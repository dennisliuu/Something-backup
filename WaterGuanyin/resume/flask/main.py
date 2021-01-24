# -*- coding: UTF-8 -*-
import json

from flask import Flask, request
from flask_cors import CORS

from moudles.house_spider import HouseSpider
from moudles import google_client_api

app = Flask(__name__, template_folder="templates")
# cors = CORS(app, resources={r"/get-house-info": {"origins": "*"}})
CORS(app)

house_spider = HouseSpider()


@app.route('/upload-video', methods=['POST'])
def upload_video_to_youtube():
    video_path = request.form['video_path']
    title = request.form['title']
    description = request.form['description']
    res = google_client_api.main(video_path, title, description)
    return json.dumps(res)


@app.route('/get-house-info', methods=['POST'])
def get_house_info():
    url = request.form['url']

    result = house_spider.parse_all_item_info_return_dict(url)
    # print(result)
    if not result:
        return json.dumps([{'status': 500}])

    return json.dumps(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8999", debug=True, use_reloader=False)
