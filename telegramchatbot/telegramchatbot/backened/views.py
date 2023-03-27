from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from telegramchatbot.utils.Responseformatter import ResponseFormatter
from rest_framework import status
from backened.service.MessageEngine import MessageEngine
from backened.service.UserDb import UserDb
from django.shortcuts import render, redirect
import requests

@api_view(['GET'])
def sampleRequest(request):
    print("inside get")
    return ResponseFormatter.formatAndReturnResponse("HELLO WORLD", status=status.HTTP_200_OK , isUI=True)

@api_view(['POST'])
def messageOperation(request):
    requestBody = JSONParser().parse(request) 
    return MessageEngine.getChatObject(requestBody)

@api_view(['GET'])
def getUser(request):
    users = UserDb.getUsers()
    return render(request,'show.html',{'users':users} )