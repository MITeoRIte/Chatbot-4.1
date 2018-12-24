import easyimap
import smtplib
import requests
from django.http import HttpResponse
import email, imaplib
import html2text
import json





# return HttpResponse("Failed")

class getmailclass():
    def getmailfunc():
        h = html2text.HTML2Text()
        h.ignore_links = True
        login = 'govtechinternship@gmail.com'
        print("login assigned")
        password = 'mcONLINE123'
        print("password assigned")
        imapper = easyimap.connect('imap.gmail.com', login, password)
        print("imap connect successful")
        for mail_id in imapper.listids(limit=1):
            print("inside for loop")
            mail = imapper.mail(mail_id)
            print(mail.body)
            incasehtml = h.handle(mail.body)
            print("HTML cleaned: " + incasehtml)
            if mail.attachments == []:
                attachments = "No attachments."
            else:
                attachments = mail.attachments

            response = (incasehtml + "\n FROM: " + mail.from_addr + " ATTATCHMENTS: " + str(attachments) + " DATE: " + str(mail.date))
            newresponse = {'mailmessage' : incasehtml, 'mailsender' : mail.from_addr, 'mailsubject' : mail.title}
            python2json = json.dumps(newresponse)
            return python2json
            break
        return python2json
    