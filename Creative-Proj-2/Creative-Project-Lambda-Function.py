
import json
import random

def getColor():
  colors = ["red","blue","green","pink","purple","indigo","cerulean","onyx","yellow"]
  color = random.choice(colors)
  return color

def lambda_handler(event, context):
    # TODO implement
    result = {
        "dialogAction":
        {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText"
            }
        }
    }

    if event["currentIntent"]["name"] == "HowHappy":
        # Do the intent 1
        upper = int(event["currentIntent"]["slots"]["upperNumber"])
        lower = int(event["currentIntent"]["slots"]["lowerNumber"])
        result["dialogAction"]["message"]["content"] = "" + \
            str(random.randint(lower, upper))
    elif event["currentIntent"]["name"] == "suggestColor":
        # Do the intent 2
        color = getColor()
        result["dialogAction"]["message"]["content"] = "I'm feeling " +color+" today"
    elif event["currentIntent"]["name"] == "sweetEmotions":
        # Do the intent 3
        # happy, sad, neutral
        emotion = event["currentIntent"]["slots"]["emotion"]
        if emotion == "happy":
           suggestion = "https://www.youtube.com/watch?v=0ymcPin-4h0"
        elif emotion == "sad":
            suggestion = "https://www.youtube.com/watch?v=Y_oD111dK7c"
        elif emotion == "neutral":
            suggestion = "https://www.youtube.com/watch?v=5qap5aO4i9A"
        result["dialogAction"]["message"]["content"] = "Here's a song suggestion: "+suggestion+""
    elif event["currentIntent"]["name"] == "AlexaCares":
        choices = ["yes","no","sure","I wish I could","a little bit","I really do"]
        choice = random.choice(choices)
        result["dialogAction"]["message"]["content"] = choice+"!"
            
        
    return result
