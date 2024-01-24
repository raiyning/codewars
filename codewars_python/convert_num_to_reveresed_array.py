# use list comprehension to fill list in and also use reveresed_strings.py to reverse number
def digitize(number):
    result = [int(x) for x in str(number)[::-1]]
    return result


example1= "123456"
example2= 123456

print(digitize(example2))