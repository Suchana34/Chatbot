from flask import Flask, request
import requests

app = Flask(__name__)

FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'

VERIFY_TOKEN = ''

PAGE_ACCESS_TOKEN = ''

def get_bot_response(message):
    return "hi,this is rosie repying to '{}'".format(message)

def verify_webhook(req):
    if req.args.get("hub.verify_token") == VERIFY_TOKEN :
        return req.args.get("hub.challenge")
    else:
        return "incorrect"

def respond(sender, message):
    #a response from a bot to the sender
    response = get_bot_response(message)
    send_message(sender, response)

def is_user_message(message):
    #checking if the message is from user
    return (message.get('message')and message['message'].get('text') and not message['message'].get("is_echo"))

@app.route("/", methods=['GET', 'POST'])

def listen():
    #flask listening to webhook
    if request.method == 'GET':
        return verify_webhook(request)
    if request.method == 'POST':
        payload = request.json
        event = payload['entry'][0]['messaging']
        for x in event:
            if is_user_message(x):
                text = x['message']['text']
                sender_id = x['sender']['id']
                respond(sender_id, text)
    return "ok"

def send_message(receipent_id, text):
    #send a response to facebook
    payload = {
        'message':{
            "text": text
        },
        'receipent':{
            "id" : receipent_id
        },
        'notification_type': 'regular'
    }

    auth = {
        'access_token': PAGE_ACCESS_TOKEN
    }

    response = requests.post(
        FB_API_URL,
        params=auth,
        json = payload
    )
    return response.json()

if __name__ == '__main__':
    app.run()