import os
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def splash():
    return render_template('index.html')


# --- EEC 172  Below ---


@app.route('/temp', methods=['GET', 'POST'])
def temp():    
    if request.method == 'GET':
        try:
            with open('./temp.txt', 'r') as f:
                return f.readlines()[0].strip()
        except Exception as e:
            print(e)
            return "-999"
    elif request.method == 'POST':
        temp = request.form.get('temp', -1)
        with open('./temp.txt', 'w') as f:
            f.write(f"{temp}")         


@app.route('/registerpush', methods=['POST'])
def register_for_push_notifications():
    token = request.form.get('token', '')
    if token:
        result = [token]
        try:
            with open('./tokens.txt', 'r') as f:
                result += [i for i in f.readlines() if i.strip()]
        except Exception as e:
            print(e)
        with open('./tokens.txt', 'w') as f:
            f.writelines(result)


@app.route('/tokens', methods=['GET'])
def get_tokens():
    try:
        with open('./tokens.txt', 'r') as f:
            'return \n'.join(f.readlines())
    except Exception as e:
        print(e)
    return e


if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 8000))