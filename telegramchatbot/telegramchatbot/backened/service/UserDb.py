from email import message
import json
from rest_framework import status
from backened.models import Telegram
from django.db.models import F
from django.db.models.functions import JSONObject
class UserDb:
      
    @classmethod
    def insertUser(cls,chat):
        try:
            userId = chat["id"]
            firstName = chat["first_name"]
            lastName = chat["last_name"]
            result = Telegram.objects.filter(UserId = userId).exists()
            result = json.loads(json.dumps(result))
            print(type(result) , result)
            if not result:
                data = Telegram(UserId = userId , UserFirstName = firstName , UserLastName = lastName , UserCount = 1)
                result2 = data.save()
                result2 = bool(json.dumps(result))
                if result2:
                    return True
            else:
                return cls.updateUser(chat)
                
        except Exception as ex:
            print('EXCEPTION AS ' , str(ex))
        return False
    
    @classmethod
    def updateUser(cls,chat):
        try:
            userId = chat["id"]
            userObj = Telegram.objects.get(UserId = userId)
            userObj.UserCount = F('UserCount') + 1
            result = userObj.save()
            result = bool(json.dumps(result))
            if result:
                return True
                       
        except Exception as ex:
            print('EXCEPTION AS ' , str(ex))
        return False
    
    @classmethod
    def getUsers(cls):
        try:
            users = Telegram.objects.all().values()
            users = list(users)
            if users:
                return users
                       
        except Exception as ex:
            print('EXCEPTION AS ' , str(ex))
        return []
    
    
 
    
