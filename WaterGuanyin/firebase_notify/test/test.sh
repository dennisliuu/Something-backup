curl -X POST \
-H 'Content-Type: application/json' \
-d '{
    "apiKey": "---",
    "deviceID": "---",
    "title": "hello",
    "message": "world"
}' \
"127.0.0.1:8999/push-notification"