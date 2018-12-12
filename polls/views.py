from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import datetime 
import os

def index(request):
    return HttpResponse("Hello, world. You are at the polls index.")

#for chatting
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
bot = ChatBot('Test')
bot.set_trainer(ListTrainer)
for f in os.listdir('/Users/yuxin/Desktop/chatterbotfiles'):
    toprocess = open('/Users/yuxin/Desktop/chatterbotfiles/' + f, 'rb').readlines()
    bot.train(toprocess)
def send_replyfromChatterbot(request):
    xinxi = request.POST['message']
    reply = bot.get_response(xinxi)
    return HttpResponse(reply)
def displaychatbot(request):
    return render(request, 'polls/converse.html')


#for getmail.html
from receivemail import getmailclass
def getamail(request):
    xinxi = request.POST['message'] #xinxi is a string
    print("value of xinxi is: " + xinxi)
    return HttpResponse(getmailclass.getmailfunc())
def getmail(request):
    return render(request, 'polls/getmail.html', {'title' : 'Chatting 4'})


#for sendmail.html
from sendmail import sendmailclass
success = False
def sendamail(request):
    reply = "Success!"
    xinxi = request.POST
    print(xinxi)
    sendmailclass.sendmailfunc(xinxi["USERNAME"],xinxi["PASSWORD"],xinxi["FROMMAIL"],xinxi["TOMAIL"],xinxi["SUBJECTTEXT"],xinxi["BODYTEXT"]) #user, password, frommail, tomail, subjecttext, bodytext
    return HttpResponse(reply)
def sendmail(request):
    return render(request, 'polls/sendmail.html', {'title' : 'Chatting2'})
