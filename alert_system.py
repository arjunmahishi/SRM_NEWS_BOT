def getStream(item):
    streams = []
    text = item.title.lower() + item.snip.lower()
    if 'b.tech' in text:
        streams.append('btech')
    if 'b.arch' in text:
        streams.append('barch')
    if 'm.tech' in text:
        streams.append('mtech')
    if 'dental' in text:
        streams.append('dental')
    return streams

def getBatch(item):
    batch = []
    text = item.title.lower() + item.snip.lower()
    if 'first year' in text or '1st year' in text or '1st semester' in text or '2nd semester' in text:
        batch.append('first year')
    if 'second year' in text or '2nd year' in text or '3rd semester' in text or '4th semester' in text:
        batch.append('second year')
    if 'third year' in text or '3rd year' in text or '5th semester' in text or '6th semester' in text:
        batch.append('third year')
    if 'fourth year' in text or '4th year' in text or '7th semester' in text or '8th semester' in text:
        batch.append('fourth year')
    return batch

# Get keywords from http://www.srmuniv.ac.in
def getKeyWords(item):
    ref = [
           'exam','change in schedule','dates', 'rescheduled','holiday',
           'holidays','timetable','urgent', 'time table', 'schedule',
           'practicals', 'postponed', 'tournaments', 'attendance'
           ] # ADD MORE #  #Sports categoory can also be added
    keyWords = []
    for e in ref:
        if e in (item.title.lower() + item.snip.lower()) and e not in keyWords:
            keyWords.append(e)
    return keyWords

def getPref(item):
    pref = []
    for e in getKeyWords(item):
        pref.append(e)
    for e in getBatch(item):
        pref.append(e)
    for e in getStream(item):
        pref.append(e)
    return pref

def newsToEmail(item,eList):
    """
      - item : One news item
      - eList : A list of all person objects
      - return : a list of validated email objects
    """
    IDs = []
    for e in eList:
        if countCommon(item.pref,e.pref) > 0:
            IDs.append(e)
    return IDs

def emailToNews(eObj,newsItems):
    """
      - eObj : an email object
      - newsItems : a list of news objects
      - return : a list of validated news objects
    """
    items = []
    for e in newsItems:
        if countCommon(eobj.pref,e.pref) > 0:
            items.append(e)
    return items

# TESTING #
#for e in news:
 #   print str(getBatch(e)) + str(getStream(e)) + str(getKeyWords(e))
