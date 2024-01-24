def generate_hashtag(sentence):
    
    # fails 1 test case use second function for all passing test cases
    if len(sentence) >=140:
        return False
    if len(sentence) ==0:
        return False
    finalHashTag = "#" + "".join(sentence.title().replace(',',' ').split())
    if len(finalHashTag) >140:
        return False
    else:
        return finalHashTag
    
def generate_hashtag2(s):
    result="#"+ str(s.title().replace(' ',''))
    return s and not len(result)>140 and result or False


print(generate_hashtag("#ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqq"))
print(generate_hashtag2("#ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqq"))