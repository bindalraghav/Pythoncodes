#common elements in 2 lists
def common_finder(l1,l2):
    output=[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output
num1=list(range(1,11))
num2=list(range(7,17))
print(common_finder(num1,num2))