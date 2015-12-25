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

def getBatch(item):
    batch = []
    if 'first year' in item.text.lower() or '1st year' in item.text.lower():
        batch.append('first year')
    if 'second year' in item.text.lower() or '2nd year' in item.text.lower():
        batch.append('second year')
    if 'third year' in item.text.lower() or '3rd year' in item.text.lower():
        batch.append('third year')
    if 'fourth year' in item.text.lower() or '4th year' in item.text.lower():
        batch.append('fourth year')
    return batch
