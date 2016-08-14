def run(str, subStr):
    """Returns a substring of any given string based upon a given range of characters before and after the substring"""

    str_range = 3

    if subStr in str:
        str_modified = str[str.index(subStr) - str_range : str.index(subStr) + len(subStr) + str_range]
        return "Mark Newman" + "\n" + str + "\n" + subStr + "\n" + str_modified
    else:
        return "ERROR: subStr not found in str!"
