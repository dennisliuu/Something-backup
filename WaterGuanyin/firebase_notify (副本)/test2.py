# Send to single device.
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AIzaSyDEB5sgzBpp20WkEVQufmit2SjLLyFFO7w")

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id = "fPzgflOGIyWDp2Z7ohsr3S:APA91bFCKThCoeLd5qEOtiFq5pq0YLfQ-sW2U_TjOct05PE60LpoeLDLM58WmXuVdek_WXBcT2E7p8tbLMqBhn1iZdVJ-a7RhS111MT64aBpwuNBwZfpEJquqk-bT-dmo6lkT52OZGSt"
message_title = "Uber update"
message_body = "Hi john, your customized news for today is ready"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

# # Send to multiple devices by passing a list of ids.
# registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
# message_title = "Uber update"
# message_body = "Hope you're having fun this weekend, don't forget to check today's news"
# result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

print(result)