name = "Suchana"
weather = "cloudy"

# Defining a dictionary with the predefined responses
responses = {
  "what's your name?": "my name is {0}".format(name),
  "what's today's weather?": "the weather is {0}".format(weather),
  "default": "default message"
}

def respond(message):
    # Check if the message is in the responses
    if message in responses:
        bot_message = responses[message]
    else:
        bot_message = responses["default"]
    return bot_message

bot_template = "BOT :{0}"
user_template = "USER : {0}"

def send_message(message):
    print(user_template.format(message))

    response = respond(message)

    print(bot_template.format(response))

send_message("what's today's weather?")
send_message("what's your name?")
