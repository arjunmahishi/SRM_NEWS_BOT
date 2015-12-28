import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

gmail_user = 'srm.news.notifier@gmail.com'
gmail_pwd = 'notifier.gmail'

obj = open('email_list.txt')
addr = obj.read().split('\n')
obj.close()

FROM = gmail_user
TO = addr
SUBJECT = 'News Updates'
# Prepare actual message
#message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
#""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
message = MIMEMultipart('alternative')
message['From'] = FROM
message['To'] = ", ".join(TO)
message['Subject'] = SUBJECT

# Create the body of the message (a plain-text and an HTML version).
text = "This is a test message.\nText and html."
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
message.attach(part1)
message.attach(part2) 

try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message.as_string())
            print "Message sent to '%s'." % TO
            server.quit()            
except smtplib.SMTPAuthenticationError as e:
            print "Unable to send message: %s" % e
