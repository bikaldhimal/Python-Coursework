
def getDate():
    import datetime
    current=datetime.datetime.now
    # print("Date: ",now().date())
    return str(current().date())

def getTime():
    import datetime
    current=datetime.datetime.now
    # print("Time: ",now().time())
    return str(current().time())
