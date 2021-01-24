importScripts('https://www.gstatic.com/firebasejs/7.6.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/7.6.0/firebase-messaging.js');
firebase.initializeApp({
  apiKey: "AIzaSyDEB5sgzBpp20WkEVQufmit2SjLLyFFO7w",
  authDomain: "fir-notification-ef3ca.firebaseapp.com",
  databaseURL: "https://fir-notification-ef3ca.firebaseio.com",
  projectId: "fir-notification-ef3ca",
  storageBucket: "fir-notification-ef3ca.appspot.com",
  messagingSenderId: "876677083697",
  appId: "1:876677083697:web:eb6b8d126f85a7fd321b10",
  measurementId: "G-9HNMM49QPK"
});
firebase.messaging();