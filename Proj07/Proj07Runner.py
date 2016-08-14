def run(str, index):
    print("Mark Newman")
    print(str)
    print(index)

    break1 = str[0:index]
    break2 = str[index - 1:len(str)]

    myList = [break1, break2]
    return myList