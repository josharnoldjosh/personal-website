import os
from time import sleep

from flask import Flask, render_template, request
from pushjack import APNSClient


app = Flask(__name__)


client = APNSClient(certificate='./key.pem',
                    default_error_timeout=10,
                    default_expiration_offset=2592000,
                    default_batch_size=100,
                    default_retries=5)


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
            return "0"
    elif request.method == 'POST':
        temp = request.form.get('temp', -1)
        with open('./temp.txt', 'w') as f:
            f.write(f"{temp}")         


@app.route('/registerpush', methods=['POST'])
def register_for_push_notifications():
    token = request.form.get('token', '')
    print("Token is:", token)
    if token:
        result = [token]
        try:
            with open('./tokens.txt', 'r') as f:
                result += f.readlines()
        except Exception as e:
            print(e)            
        with open('./tokens.txt', 'w') as f:
            f.writelines(list(set(result)))
            print(f"Wrote result: {result}")
    return "success!"


@app.route('/tokens', methods=['GET'])
def get_tokens():
    try:
        with open('./tokens.txt', 'r') as f:
            return '\n'.join(f.readlines())
    except Exception as e:
        print(e)
    return ""


@app.route('/notify', methods=['POST'])
def notify_all():

    temp = "0"
    try:
        with open('./temp.txt', 'r') as f:
            temp = f.readlines()[0].strip()
    except Exception as e:
        print(e)    

    delay = request.form.get('delay', 2)
    
    sleep(float(delay))

    alert=f"Your temperature has changed: {temp}˚F"

    tokens = get_tokens().split('\n')
    for token in tokens:        
        print("Sending for", token)
        res = client.send(token, alert)        
        print(res.errors, res.tokens, res.token_errors)
        
    return "success!"


if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 8000))