#sum of the number in list in form of list
def sqr_of_list(num):
    square=[]
    for i in num:
        square.append(i**2)
    return square

number=list(range(1,11))
print(number)
print(sqr_of_list(number))
