import urllib2, datetime, sendmail_SMTP, marriage
from bs4 import BeautifulSoup

class newsItem:
    def __init__(self,title,link,snip):
        self.title = title
        self.snip = snip
        self.link = link

def displayAllNews(news):
    for i in range(len(news)):
        print str(i+1) + ". " + news[i].title

def getNews():
    news = []
    try:
        data1 = urllib2.urlopen("http://www.srmuniv.ac.in/Announcements").read()
        data2 = urllib2.urlopen("http://www.srmuniv.ac.in/University-News").read()
        soup1 = BeautifulSoup(data1,'html.parser')
        soup2 = BeautifulSoup(data2,'html.parser')
        for tag in soup1.find_all('div',{'class':'col-lg-10  col-xs-10 col-sm-10 col-md-10 latest-text padding-left-10px'}):
            title = tag.find_all('h4')[0].text
            link = "http://www.srmuniv.ac.in" + tag.find_all('a')[0].get('href')
            snip = tag.find_all('p')[0].text.replace('... More','...')
            news.append(newsItem(title,link,snip))

        for tag in soup2.find_all('div',{'class':'col-lg-10  col-xs-10 col-sm-10 col-md-10 latest-text padding-left-10px'}):
            title = tag.find_all('h4')[0].text
            link = "http://www.srmuniv.ac.in" + tag.find_all('a')[0].get('href')
            snip = tag.find_all('p')[0].text.replace('... More','...')
            news.append(newsItem(title,link,snip))
    except urllib2.URLError:
        return "fail"
    return news

def getNewNews():
    file_name = "old_news.txt"
    obj = open(file_name)
    oldNews = obj.read().split('\n')
    news = getNews()
    if news == 'fail':
        return "fail"
    newNews = []
    for item in news:
        if item.title not in oldNews:
            newNews.append(item)
    obj.close()
    return newNews

def updateFile(newNews):
    obj = open('old_news.txt','a')
    for item in newNews:
        obj.write(item.title.encode('UTF-8') + '\n')
    obj.close()

def updateLog(msg):
    '''
        -This function will update the status of the bot
         everytime it is executed. All the data goes into
         'logfile.txt'
        -This will help monitor the bot for problems.
    '''
    log = open('logfile.txt','a')
    log.write(str(datetime.datetime.now()) + " : " + str(msg) + '\n')
    log.close()

if __name__ == '__main__':
    newNews = getNewNews()
    print str(len(newNews)) + ' new items'
    addr = sendmail_SMTP.getEmailData()
    if newNews == 'fail':
        print "Not able to reach SRM"
        updateLog("Not able to reach SRM")
    elif len(newNews) == 0:
        print "Nothing new on the website"
        updateLog("Nothing new on the website")
    else:
        if len(newNews) == 1:
            rec = marriage.newsToEmail(newNews[0],addr)
            sendmail_SMTP.sendMail(newNews,rec)
            displayAllNews(newNews)
        else:
            for e in addr:
                neededNews = marriage.emailToNews(e,newNews)
                sendmail_SMTP.sendMail(newNews,e)
                displayAllNews(neededNews)
        updateLog(str(len(newNews)) + " news items are new!")
        updateFile(newNews)
    #raw_input() # hold
