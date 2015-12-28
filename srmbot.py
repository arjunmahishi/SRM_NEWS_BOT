import urllib2
from bs4 import BeautifulSoup
import datetime

class newsItem:
    def updateScore(self,score):
        self.score = score
    def __init__(self,text):
        self.text = text
        self.score = 0

def displayAllNews(news):
    for i in range(len(news)):
        print str(i+1) + ". " + news[i].text

def getNews():
    news = []
    try:
        data = urllib2.urlopen("http://www.srmuniv.ac.in").read()
        soup = BeautifulSoup(data,'html.parser')
        for tag in soup.find_all('div',{'class':'views-field views-field-title'}):
            news.append(newsItem(tag.text.strip()))
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
        if item.text not in oldNews:
            newNews.append(item)
    obj.close()
    return newNews

def updateFile(newNews):
    obj1 = open('old_news.txt','a')
    abj2 = open('new_news.txt','a')
    for item in newNews:
        obj1.write(item.text + '\n')
        obj2.write(item.text + '\n')
    obj1.close()
    obj2.close()

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
    if newNews == 'fail':
        print "Not able to reach SRM"
        updateLog("Not able to reach SRM")
    elif len(newNews) == 0:
        print "Nothing new on the website"
        updateLog("Nothing new on the website")
    else:
        displayAllNews(newNews)
        updateLog(str(len(newNews)) + " news items are new!")
    updateFile(newNews)
    raw_input() # hold
