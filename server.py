import os
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def splash():
    return render_template('index.html')


# ~~ EEC 172 - Final Project ~~


@app.route('/temp', methods=['GET', 'POST'])
def temp():    
    if request.method == 'GET':
        try:
            with open('./temp.txt', 'r') as f:
                return f.readlines()[0].strip()
        except Exception as e:
            print(e)
            return -999
    elif request.method == 'POST':
        temp = request.form.get('temp', -1)
        with open('./temp.txt', 'w') as f:
            f.write(f"{temp}")            


if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 8000))