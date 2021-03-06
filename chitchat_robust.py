import random

name = "Suchana"
weather = "cloudy"

responses = {
  "what's your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "what's today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ],
  "default": ["default message"]
}

# Use random.choice() to choose a matching response
def respond(message):
    if message in responses:
        bot_message = random.choice(responses[message])
    else:
        bot_message = random.choice(responses["default"])
    return bot_message

bot_template = "BOT :{0}"
user_template = "USER : {0}"

def send_message(message):
    print(user_template.format(message))

    response = respond(message)

    print(bot_template.format(response))

send_message("what's today's weather?")
send_message("what's today's weather?")
send_message("what's today's weather?")
