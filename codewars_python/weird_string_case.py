def to_weird_case(words):
    result = ''
    if ' ' in words:
        for word in words.split(' '):
            result = result + to_case_change(word) + ' '
        return  result[:-1]
    else:
        result = to_case_change(words)
        return  result

def to_case_change(word):
    result = ''
    for index, char in enumerate(word):
        if char ==' ':
            print()
        if index % 2 == 0:
            result = result + char.upper()
        if index % 2 == 1:
            result = result + char.lower()
    return result

# codewars top voted solution
# def to_weird_case_word(string):
#     return "".join(c.upper() if i%2 == 0 else c for i, c in enumerate(string.lower()))
    
# def to_weird_case(string):
#     return " ".join(to_weird_case_word(str) for str in string.split())

print(to_weird_case('Weird string case'))