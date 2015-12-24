import smtplib
import string
import srmbot

news = srmbot.getNews()

From = "srm_news_notifier@yahoo.com"
To = []
Subj = "Important News"
Text = ""
password = "warlock111"
for e in range(len(news)):
    Text += str(e+1) + ". " + news[e].text + '\n\n'

Body = string.join((
        "From: %s" % From,
        "To: %s" % To,
        "Subject: %s" % Subj,
        "",
        Text,
        ), "\r\n") 

try:
    server = smtplib.SMTP('smtp.mail.yahoo.com:587')
    server.starttls()
    server.login(From,password)
    server.sendmail(From,To,Body)
    server.quit()
    print "EMAIL SENT"
except:
    print "EMAIL NOT SENT"
