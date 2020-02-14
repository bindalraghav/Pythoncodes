def reverselist(num):
    reverse=[]
    for i in range(len(num)):
       poped_item=num.pop()
       reverse.append(poped_item)
    return reverse

number=list(range(1,11))
print(number)
print(reverselist(number))