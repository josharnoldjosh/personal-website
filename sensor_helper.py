import random

import requests


def send_temperature(temp_f):
    """
    Sends a temperature as a numeric type
    to the server, which from there propergates
    the value to the mobile app.

    temp_f : a numeric temperature in fahrenheit.
    Example: send_temperature(92.7)
    """        
    requests.post(
        "https://www.josharnold.me/temp", 
        data = {'temp': f"{temp_f:.1f}"}
    )


def get_temperature():
    """
    Returns the temperature as an int. Will return
    -1 if no temperature has been set.
    """
    return requests.get('https://www.josharnold.me/temp').json()


if __name__ == '__main__':    
    send_temperature(random.uniform(60.0, 85.0))
    result = get_temperature()    
    print(f"The temperature is {result} ℉")