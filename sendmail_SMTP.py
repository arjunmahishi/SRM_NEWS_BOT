import smtplib, base64, datetime
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class person:
        def __init__(self,name,emailID,pref):
                self.name = name
                self.emailID = emailID
                for e in range(len(pref)):
                        pref[e] = pref[e].replace('"','')
                        pref[e] = pref[e].replace(' ','')
                self.pref = pref

def getHTML(newNews):
        obj = open("index.html")
        items = ""
        """<tr>
                    <td style=\"font-size: 13px; color: #959595; font-weight: normal; text-align: left; font-family: Georgia, Times, serif; line-height: 24px; vertical-align: top; padding:10px 8px 10px 8px\" bgcolor=\"#eeeeed\">
                        <table>
                            <tr>
                                <td valign=\"middle\" style=\"padding:0 10px 10px 0\"><a href=\"newNews[i].link\" style=\"text-decoration: none; color: #272727; font-size: 20px!important; color: #272727; font-weight: bold; font-family:Arial, sans-serif\">newNews[i].title</a>
                                </td>
                            </tr>
                        </table>	
                             <p style=\"font-size: 250% !important;\">newNews[i].snip</p>
						 </td>
                </tr>"""
        for i in range(len(newNews)):
              item = '<tr><td style="font-size: 13px; color: #959595; font-weight: normal; text-align: left; font-family: Georgia, Times, serif; line-height: 24px; vertical-align: top; padding:10px 8px 10px 8px" bgcolor="#eeeeed"><table><tr><td valign="middle" style="padding:0 10px 10px 0\"><a href="'
              item += newNews[i].link + '" style="text-decoration: none; color: #272727; font-size: 20px!important; color: #272727; font-weight: bold; font-family:Arial, sans-serif">'
              item += newNews[i].title + '</a></td></tr></table><p style="font-size: 250% !important;">' + newNews[i].snip + '</p></td></tr>'
              items += item.encode('UTF-8')
        html = obj.read()
        html = html.replace("--contents--", items)
        return html

def getEmailData():
        # Don't bother to understand. Because nither do I. It just works.
        eList = []
        obj = open('email_data.csv')
        emailList = obj.read().split('\n')
        temp = []
        for e in emailList[1:]:
                temp.append(e.split(',')[1:])
        emailList = temp
        obj.close()
        for e in emailList:
                eList.append(person(e[0],e[1],e[2:]))
        return eList
        

def sendMail(newNews, temp):
        """
          newNews : a list of newsItems to be sent to the given user(s).
          addr : a list of emailIDs. May contain 1 or more email IDs
        """
        addr = []
        try:
                for e in temp:
                        addr.append(e.emailID)
        except TypeError:
                addr.append(temp.emailID)
        gmail_user = 'srm.news.notifier@gmail.com'
        gmail_pwd = base64.b64decode("MTIwMG5vdGlmeS5tZQ==")
        
        FROM = gmail_user
        TO = addr
        print TO
        #now = datetime.datetime.now()
        SUBJECT = 'News updates'
        
        message = MIMEMultipart('alternative')
        message['From'] = FROM
        message['Bcc'] = ", ".join(TO)
        message['Subject'] = SUBJECT
# Create the body of the message (a plain-text and an HTML version).
        text = "This is a test message.\nText and html."
        html = getHTML(newNews)
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
                print "Mail sent to '%s'." % addr
                server.quit()            
        except smtplib.SMTPAuthenticationError as e:
                print "Unable to send mail: %s" % e

if __name__ == '__main__':
        l = getEmailData()
