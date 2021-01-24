# -*- coding: UTF-8 -*-
import json

from flask import Flask, request
from flask_cors import CORS

from moudles import push_notify

app = Flask(__name__, template_folder="templates")
# cors = CORS(app, resources={r"/get-house-info": {"origins": "*"}})
CORS(app)

@app.route('/push-notification', methods=['POST'])
def push_notification():
    data = request.get_json()
    apiKey = data['apiKey']
    deviceID = data['deviceID']
    title = data['title']
    message = data['message']
    res = push_notify.main(apiKey, deviceID, title, message)

    return json.dumps(res)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8999", debug=True, use_reloader=False)