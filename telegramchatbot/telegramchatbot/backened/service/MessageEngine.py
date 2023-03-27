from email import message
import json
from rest_framework import status
import requests, random
import pyjokes
from telegramchatbot.utils.Responseformatter import ResponseFormatter
from backened.service.UserDb import UserDb
class MessageEngine:
    
    @classmethod
    def getChatObject(cls,chatObject):
        message = chatObject["message"]
        chat = message["chat"]
       
        UserDb.insertUser(chat, message['text'])
        print("chatobject" , chatObject)
        result = cls.sendMessage(chat  , message['text'])
        if result:
            return ResponseFormatter.formatAndReturnResponse("SUCCESS", status=status.HTTP_200_OK , isUI=True)
        else:
            return ResponseFormatter.formatAndReturnResponse("FALSE", status=status.HTTP_500_INTERNAL_SERVER_ERROR , isUI=True)
    
    @classmethod
    def sendMessage(cls,chat , user_option):
        try:
            joke = cls.getJoke() 
            text = joke
            if user_option == '/dumb':
                text = f"{chat['first_name']} , U are not dumb but this joke will make U!!!" + joke
            elif user_option == '/stupid':
                text = f"Get some intelligence dear {chat['first_name']} . Don't spend your time in stupid things " + joke
            elif user_option == '/fat':
                text = f"{chat['first_name']} has reduced 0.001 calories of weight" + joke
            
        
            print(joke)
            message_data = {
                "chat_id": chat['id'],
                "text": text,
                "parse_mode": "Markdown",
            }
            print(message_data)
            message_url = 'https://api.telegram.org/bot6186522246:AAEDC16pEhykVWfvJN5aMxZ2Wyya2EGfyKU/sendMessage'
            response = requests.post(message_url, json = message_data) 
            if response.status_code == status.HTTP_200_OK:
                return True
        except Exception as ex:
            print('EXCEPTION AS ' , str(ex))
        return False
    
    
    @classmethod
    def getJoke(cls):
        try:
            joke = pyjokes.get_joke(language="en", category="all")
            print("JOKE" , joke)
            print("TYPE",type(joke))
            joke = json.dumps(joke)
            return joke
        except Exception as ex:
            return "Always be happy!!!"
    
    
