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
            apiKey: "---",
            authDomain: "---",
            databaseURL: "---",
            projectId: "---",
            storageBucket: "---",
            messagingSenderId: "---",
            appId: "---",
            measurementId: "---"
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