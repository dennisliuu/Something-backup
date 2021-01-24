import requests
import json

payload = {
    'DOMODE': 'doFASTCALL',
    'SvcType': '0',
    'OrderID': 'WDS201911291800322612325618630',
    'FullOrderID': '47834690304861253307590020249997621669956638712109',
    'Phone': '0921196446',
    'COUNTRYCODE': '886',
    'CustTitle': 'd先生',
    'CUSTACCT': '0921196446',
    'CustName': 'd先生',
    'City': '新北市',
    'Distrcit': '淡水區',
    'Road': '自強路',
    'Section': 'null',
    'Lane': '116巷',
    'Alley': '1弄',
    'No': '1號',
    'PaidType': '1',
    'SpecOrder': '0,0,0,0,0,0,0,0,0,0,0,0',
    'ST': '1',
    'Address': '新北市|淡水區|自強路||116巷|1弄|1號',
    'Lng_X': '121.4636',
    'Lat_Y': '25.13218',
    'Memo': ''
}
cookies = {'ASP.NET_SessionId':'wrqm320ci0hbalmgugbbmiwz','ValidateCode':'460442', 'ValidateToken':'gm3sux50qleif7ys6x0ql8cj4jtiqprdfo98'}

r = requests.post("https://wds.taiwantaxi.com.tw/APPS/Booking/New_Calldispath.aspx", data=payload, cookies=cookies)
print(r.text)
parsed = json.loads(r.text)
print(json.dumps(parsed, indent=4, sort_keys=True))