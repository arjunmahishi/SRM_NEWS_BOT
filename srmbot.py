import urllib2
from bs4 import BeautifulSoup

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
        print "Internet not working"
    return news

if __name__ == '__main__':
    news = getNews()
    displayAllNews(news)
    raw_input() # hold
