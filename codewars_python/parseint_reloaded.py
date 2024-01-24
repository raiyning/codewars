
def zeros(n):
    result=0
    counter=1
    while n//(5**counter) > 0:
        print("start loop, result is starting with {} and counter value is {}".format(result,counter))
        result = result + n//(5**counter)
        counter+=1
        print("end loop, result is {} and counter is {}".format(result, counter))
    return 

print(zeros(4617))