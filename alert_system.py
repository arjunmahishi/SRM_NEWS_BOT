import srmbot

news = srmbot.getNews()

def getStream(item):
    streams = []
    if 'b.tech' in item.text.lower():
        streams.append('btech')
    if 'b.arch' in item.text.lower():
        streams.append('barch')
    if 'm.tech' in item.text.lower():
        streams.append('mtech')
    if 'dental' in item.text.lower():
        streams.append('dental')
    return streams

d = {}

for i in range(len(news)):
    d[news[i].text] = getStream(news[i])
    
for w in news:
    print str(w.text) + " : " + str(d[w.text])
