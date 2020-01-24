#create templates
from echobot1 import respond;

bot_template = "BOT :{0}"
user_template = "USER : {0}"

def send_message(message):
    print(user_template.format(message))

    response = respond(message)

    print(bot_template.format(response))

send_message("hello")
