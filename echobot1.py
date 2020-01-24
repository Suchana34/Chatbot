bot_template = "BOT :{0}"
user_template = "USER :{0}"

#a function that responds to the bot message
def respond(message):
    bot_message = "I can hear you! You said: " + message
    
    return bot_message

print(respond("hello !")) 