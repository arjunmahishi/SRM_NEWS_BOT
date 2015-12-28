import smtplib
from multiprocessing import Process
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import srmbot

def sendMail():
	gmail_user = 'srm.news.notifier@gmail.com'
	gmail_pwd = 'notifier.gmail'
	newNews = srmbot.getNewNews() # list of new news
	obj2 = open('email_list.txt')
	addr = obj2.read().split('\n')
	obj2.close()

	FROM = gmail_user
	TO = addr
	SUBJECT = 'News Updates'
	TEXT = ""   ##################### Create a templet 

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

if __name__ == '__main__':
	sendMail()
	raw_input()
