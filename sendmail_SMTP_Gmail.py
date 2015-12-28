import smtplib
from multiprocessing import Process
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

gmail_user = 'srm.news.notifier@gmail.com'
gmail_pwd = raw_input("Enter the GMail password:")

obj1 = open('new_news.txt', 'r')
obj2 = open('email_list.txt', 'r')
FROM = gmail_user
TO = addr
SUBJECT = 'News Updates'
TEXT = obj1.read()
with open('email_list.txt') as f:
    addr = f.readlines()

# Prepare actual message
message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            print "Message sent to '%s'." % TO
            server.quit()
            
except smtplib.SMTPAuthenticationError as e:
            print "Unable to send message: %s" % e
