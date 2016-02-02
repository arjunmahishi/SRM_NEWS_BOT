def countCommon(L1,L2):
    count = 0
    temp = []
    for a in L2:
        temp.append(a.lower())
    L2 = temp
    for e in L1:
        if e.lower() in L2:
            count += 1
    return count 

def getBatch(item):
    batch = []
    text = item.title.lower() + " " + item.snip.lower()
    if 'first year' in text or '1st year' in text or '1st semester' in text or '2nd semester' in text:
        batch.append('first')
    if 'second year' in text or '2nd year' in text or '3rd semester' in text or '4th semester' in text:
        batch.append('second')
    if 'third year' in text or '3rd year' in text or '5th semester' in text or '6th semester' in text:
        batch.append('third')
    if 'fourth year' in text or '4th year' in text or '7th semester' in text or '8th semester' in text:
        batch.append('fourth')
    return batch

# Get keywords from http://www.srmuniv.ac.in
def getKeyWords(item):
    imp = [
           'exam', 'exams', 'change in schedule', 'date', 'dates', 'rescheduled','holiday',
           'holidays','timetable','urgent', 'time table', 'schedule', 'scheduled',
           'practicals', 'postponed', 'attendance', 'examination', 'examinations'
           ] # ADD MORE #
    events_n_sports = [
                    'tournament', 'tournaments', 'game', 'tennis', 'won', 'venue'
                  ]
    univ = [
              'passed', 'closed', 'reopen', 'reopened'
            ]
    keyWords = []
    for e in imp:
        if e in (item.title.lower() + item.snip.lower()).split(' ') and e not in keyWords:
            keyWords.append('AcademicNews')
            break
    for e in events_n_sports:
        if e in (item.title.lower() + item.snip.lower()).split(' '):
            keyWords.append('Events/Sports')
            break

    for e in univ:
        if e in (item.title.lower() + item.snip.lower()).split(' '):
            keyWords.append('UniversityUpdates')
            break
    
    return keyWords

def getPref(item):       #Gets Complete info about the news item
    pref = []
    for e in getKeyWords(item):
        pref.append(e)
    for e in getBatch(item):
        pref.append(e)
    if len(pref) == 0:
        pref.append("UniversityUpdates")
    return pref

def newsToEmail(item,eList):
    """
      - item : One news item
      - eList : A list of all person objects
      - return : a list of validated email objects
    """
    IDs = []
    for e in eList:
        print getPref(item)
        if countCommon(getPref(item),e.pref) > 0: 
            IDs.append(e)
    return IDs

def emailToNews(eObj,newsItems):
    """
      - eObj : one email object
      - newsItems : a list of news objects
      - return : a list of validated news objects
    """
    items = []
    for e in newsItems:
        if countCommon(eObj.pref,getPref(e)) > 0:
            items.append(e)
    return items
