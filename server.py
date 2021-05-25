import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def splash():
    return render_template('index.html')


# ~~ EEC 172 - Final Project ~~


global CURRENT_TEMP
CURRENT_TEMP = -1


@app.route('/set_temp/<temp>')
def set_temp(temp):
    global CURRENT_TEMP
    CURRENT_TEMP = temp
    return "Success!"


@app.route('/get_temp')
def get_temp():
    return CURRENT_TEMP


if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 8000))