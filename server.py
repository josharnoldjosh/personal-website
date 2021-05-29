import os
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def splash():
    return render_template('index.html')


# ~~ EEC 172 - Final Project ~~


global CURRENT_TEMP
CURRENT_TEMP = [-1]


@app.route('/temp', methods=['GET', 'POST'])
def temp():            
    global CURRENT_TEMP
    if request.method == 'GET':
        return f"{CURRENT_TEMP[0]}"
    elif request.method == 'POST':
        CURRENT_TEMP[0] = request.form.get('temp', -1)    


if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 8000))