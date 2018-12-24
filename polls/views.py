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
trainerset = []
for f in os.listdir('/Users/yuxin/Desktop/chatterbotfiles'):
    with open('/Users/yuxin/Desktop/chatterbotfiles/' + f, encoding="utf-16") as toprocess:
        for line in toprocess:
            linestripped = str(line).rstrip("b'")
            linefinal = linestripped.rstrip("\n'")
            print(str(linefinal))
            trainerset.append(str(linefinal))
        bot.train(trainerset)
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
    print("sendamail function invoked")
    reply = "Mail sent!"
    xinxi = request.POST
    print(xinxi)
    try:
        print("send mail requested")
        sendmailclass.sendmailfunc(xinxi["USERNAME"],xinxi["PASSWORD"],xinxi["FROMMAIL"],xinxi["TOMAIL"],xinxi["SUBJECTTEXT"],xinxi["BODYTEXT"]) #user, password, frommail, tomail, subjecttext, bodytext
        print("send mail passed.")
    except:
        print("send mail failed.")
    return HttpResponse(reply)
def sendmail(request):
    return render(request, 'polls/sendmail.html', {'title' : 'Chatting2'})
