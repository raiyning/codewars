# parseint trailing 0's for a factorial number
def zeros(n):
    result=0
    counter=1
    while n//(5**counter) > 0:
        result+=n//(5**counter)
        counter+=1
    return result

print(zeros(4617))