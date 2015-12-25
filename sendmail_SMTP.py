import smtplib, os

#Getting data , Function can also be used
user = 'srm.news.notifier@gmail.com'
pwd = 'notifier.gmail'
recipient = 'srm.news.notifier@gmail.com'
subject = 'Test'
body = 'testing via SMTP'


gmail_user = user
gmail_pwd = pwd
FROM = user
TO = recipient if type(recipient) is list else [recipient]
SUBJECT = subject
TEXT = body

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
            print 'successfully sent the mail'
except:
            print "failed to send mail"
