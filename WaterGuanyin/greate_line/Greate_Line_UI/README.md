ReadMe
=======
## Execute
* Check if installed electron globally: `$ electron --version `
  * If not installed yet, install it.(`$ npm install -g electron`)
* Run electron with this prject root path: `$ electron .`

## File Structure
* html/ -> storing frontend
* index.js -> program entry

## Update Records
### Update by 宇宸 @ 2019/5/27
* WebSocket 描述：
  * 位置：assets/js/websocket2.js
  * 建立：WS(url, debug = false, skipConnect = false)
    * 對 `url` 建立連線
    * 當 debug = true，觸發事件時輸出到 console.info
    * 當 skipConnect = true，不立即連接（需自行 .connect() ）
  * 使用 .on 註冊事件：on(order, callback)
    * 收到資料時，根據對應 order 執行回呼，callback 接受一個參數 detail，其餘參數與資料將會忽略
    * 若要收取完整資料，註冊 `$message`
  * 使用 .once 註冊單次事件，格式同上，當 callback 呼叫後移除監聽
  * 使用 .send 發送資料：send(order, detail)
    * 將會包裝成字串
  * 使用 .reconnect 重新連線：reconnect(newurl)
    * 當 newurl 為空，則對啟動時進行連線
  * 使用 .trigger 觸發事件：trigger(order, ...data)
    * `$error`, `$open`, `$close`, `$message` 會註冊到原生 WebSocket 事件上
    * 其餘者，檢查 listener 是否有可呼叫 callback，若有則迭代呼叫
### Init by 宇宸 @ 2019/5/23
* index.html Vue instance 數據描述：
  * newAccount -> 新增帳戶欄位
  * accounts -> 既有的帳戶資料
  * liveUrl -> 新增直播間欄位的網址
  * lives -> 既有的直播間資料
  * liveMeta -> 直播間元資料
  * commentSetting -> 對話控制