Firebase Cloud Message
===

使用套件：![PyFCM](https://github.com/olucurious/PyFCM)

1. 申請 Firebase application
2. 在 cloud messahe tab 中取得 FCM apikey
3. 取得 token (device id)，每臺機器不同 (list type)
    - Android / iOS 同樣先取得 deviceID 後即可使用
4. POST /push-notification with apikey, device, title, message