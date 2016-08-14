import re

def run(aTuple, aWord):
    print("Mark Newman")
    print(aWord)
    print(aTuple)

    p = re.compile(aWord)
    aList = filter(lambda aWord : p.search(aWord), aTuple)

    #The below code is *almost* the same as the above combined filter and lambda statements.  The difference is that the above list is constructed with the returned filter values.  I am guessing it is faster but has the possibility of using more "temporary" memory?
    #aList = []
    #for str in aTuple:
    #    m = p.search(str)
    #    if m:
    #        aList.append(str)

    return aList