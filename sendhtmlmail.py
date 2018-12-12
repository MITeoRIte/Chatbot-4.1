from mailer import Mailer
from mailer import Message
import smtplib

message = Message(From="govtechinternship@gmail.com",
                  To="govtechinternship@gmail.com")
message.Subject = "An HTML Email"
message.Html = """<p>Hi!<br>
   How are you?<br>
   Here is the <a href="http://www.python.org">link</a> you wanted.</p>"""
gmail_user = "govtechinternship@gmail.com"
gmail_password = "mcONLINE123"
sender = smtplib.SMTP_SSL('smtp.gmail.com', 465)
sender.login(gmail_user, gmail_password)

sender.send(message)
