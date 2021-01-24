from pyfcm import FCMNotification

def main(api_key, deviceID, title, message):

    # Single Device
    push_service = FCMNotification(api_key=api_key)
    registration_id = deviceID
    message_title = title
    message_body = message
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

    # Multi Device (only registration_ids different)
    # registration_ids = deviceID
    # message_title = title
    # message_body = message
    # result = push_service.notify_single_device(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

    return result

if __name__ == "__main__":
    main("", "", "hello", "world")