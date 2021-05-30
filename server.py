import os
from time import sleep

from flask import Flask, render_template, request

from eec_helper import (
    get_temp,
    write_temp,
    send_notifications
)


app = Flask(__name__)


@app.route('/')
def splash():
    return render_template('index.html')


@app.route('/temp', methods=['GET', 'POST'])
def temp():    
    """
    Temporary for EEC 172.
    Will send a push notification if the 
    change in temperature is greater than
    5 degrees.
    """
    if request.method == 'GET':
        return get_temp()
    elif request.method == 'POST':
        temp = request.form.get('temp', -1)
        delta = float(temp) - float(get_temp())
        if abs(delta) >= 5:
            key = "dropped" if delta < 0 else "risen"
            send_notifications(
                title="EEC 172",
                body=f"Your home temperature has {key} to {temp}˚F"
            )        
        write_temp(temp)


if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 8000))