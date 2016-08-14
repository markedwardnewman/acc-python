def run (aList, aChar):
    print("Mark Newman")
    print(aChar)
    print(aList)
    filteredList = []

    for word in aList:
        if aChar not in word:
            filteredList.append(word)

    return filteredList