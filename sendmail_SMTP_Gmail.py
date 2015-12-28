import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

gmail_user = 'srm.news.notifier@gmail.com'
gmail_pwd = raw_input("Enter the GMail password:")

obj1 = open('new_news.txt')
obj2 = open('email_list.txt')
recipient = obj2.read()
FROM = gmail_user
TO = recipient if type(recipient) is list else [recipient]
SUBJECT = 'News Updates'
TEXT = obj1.read()

# Prepare actual message
message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            server.quit()
            print 'Successfully sent the mail'
except:
            print "Unable to send message, try again"
