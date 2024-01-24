def solution(stringLine):

    newList = [stringLine[i:i+2] for i in range(0, len(stringLine), 2)]
    if (len(stringLine) % 2) == 1:
        print(True)
        newList[-1] = newList[-1] + "_"
    return newList

    


print(solution("asdfads"))