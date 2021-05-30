from pusher_push_notifications import PushNotifications


def send_notifications(title, body):
    """
    Sends a push notification to all 
    devices.
    """
    beams_client = PushNotifications(
        instance_id='d4e8064a-36fa-49f1-8449-1cd616819682',
        secret_key='CC49486F73D82BCAC8CA8F5423253BD69B12B94DA5CB8A1F46DC252764A704D0',
    )

    response = beams_client.publish_to_interests(
        interests=['hello'],
        publish_body={
            'apns': {'aps': {'alert': { 'title': title, 'body': body}}},
            'fcm': {'notification': {'title': title, 'body': body}},
            'web': {'notification': {'title': title, 'body': body}}
        }
    )

    print(response['publishId'])
    return
    

def get_temp():
    """
    Returns the temperature as a 
    string from a temporary file.
    """
    try:
        with open('./temp.txt', 'r') as f:
            return f.readlines()[0].strip()
    except Exception as e:
        print(e)
        return "0"


def write_temp(temp):
    """
    Writes the temperature as a 
    string from a temporary file.
    """
    with open('./temp.txt', 'w') as f:
        f.write(f"{temp}")