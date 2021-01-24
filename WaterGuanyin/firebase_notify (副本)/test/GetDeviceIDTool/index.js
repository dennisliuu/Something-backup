const path = require('path');
const express = require('express');
const app = express();
app.use(
  '/firebase-messaging-sw.js',
  express.static(path.resolve(__dirname, '../test-js/js/firebase-messaging-sw.js'))
);
console.log(path.resolve(__dirname, '../test-js/js/firebase-messaging-sw.js'))
app.get('/', (req, res) => {
    res.send(`
    <html>
      <head></head>
      <body>
        <h1>Push Notification</h1>
        <script src="https://www.gstatic.com/firebasejs/7.6.0/firebase-app.js"></script>
        <script src="https://www.gstatic.com/firebasejs/7.6.0/firebase-messaging.js"></script>

        <script>
          var firebaseConfig = {
            apiKey: "AIzaSyDEB5sgzBpp20WkEVQufmit2SjLLyFFO7w",
            authDomain: "fir-notification-ef3ca.firebaseapp.com",
            databaseURL: "https://fir-notification-ef3ca.firebaseio.com",
            projectId: "fir-notification-ef3ca",
            storageBucket: "fir-notification-ef3ca.appspot.com",
            messagingSenderId: "876677083697",
            appId: "1:876677083697:web:eb6b8d126f85a7fd321b10",
            measurementId: "G-9HNMM49QPK"
          };
          firebase.initializeApp(firebaseConfig);
          const messaging = firebase.messaging();
          messaging
            .requestPermission()
            .then(function() {
              console.log('Notification permission granted.');
            })
            .catch(function(err) {
              console.log('Unable to get permission to notify.', err);
            });
          messaging.getToken()
            .then((currentToken) => {
              console.log(currentToken)
            })
          messaging.onTokenRefresh(() => {
            messaging.getToken()
              .then((refreshToken) => {
                console.log('Token refresh')
              })
          })
          messaging.onMessage((payload) => {
            console.log('Message received.', payload)
          })
        </script>
      </body>
    </html>
  `);
});
app.listen(8998);

// token = fPzgflOGIyWDp2Z7ohsr3S:APA91bFCKThCoeLd5qEOtiFq5pq0YLfQ-sW2U_TjOct05PE60LpoeLDLM58WmXuVdek_WXBcT2E7p8tbLMqBhn1iZdVJ-a7RhS111MT64aBpwuNBwZfpEJquqk-bT-dmo6lkT52OZGSt
