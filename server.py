import os
from time import sleep

from flask import Flask, render_template, request

from eec_helper import (
    get_temp,
    write_temp    
)


app = Flask(__name__)


@app.route('/')
def splash():
    return render_template('index.html')


# ~~~ EEC 172 ~~~


@app.route('/temp', methods=['GET', 'POST'])
def temp():    
    if request.method == 'GET':
        return get_temp()
    elif request.method == 'POST':
        temp = request.form.get('temp', -1)
        write_temp(temp)


@app.route('/notify', methods=['POST'])
def notify_all():
    temp = get_temp()
    alert = f"Your home temperature has dropped to {temp}˚F"        
    return "success!"


if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 8000))