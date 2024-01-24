def likes(names):
    result=""
    if names == []:
        result = "no one likes this"
    if len(names) ==1:
        result = "{name} likes this".format(name = names[0])
    if len(names) > 1 and len(names) <= 3:
        commaNames = "".join(name+", " for name in names[0:-2] )
        result = "{namelist}{secondLastName} and {nameLastList} like this".format(namelist = commaNames, nameLastList=names[-1], secondLastName=names[-2] )
    if len(names) > 3:
        commaNames = names[0] + ", " + names[1]
        result = "{namelist} and {remainingNamesNumber} others like this".format(namelist = commaNames, remainingNamesNumber=len(names)-2)
    return result

print(likes(['Alex', 'Jacob', 'Mark', 'Max']))


def likesSolution(names):
    # make a dictionary d of all the possible answers. Keys are the respective number
    # of people who liked it.
    
    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = length - 2"
    # is passed to str.format()
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
        }
    length = len(names)
    # d[min(4, length)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4
    
    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = length - 2
    return d[min(4, length)].format(*names, others = length - 2)
