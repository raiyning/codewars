def to_camel_case(word):
    if word == "": return ""
    joinedword = word.replace("-","_")
    joinedword = ''.join(x.capitalize() or '_' for x in joinedword.split('_'))
    if word.islower() == True:
       return joinedword.lower() +joinedword
    return joinedword

    
print(to_camel_case("the_stealth_warrior"))  