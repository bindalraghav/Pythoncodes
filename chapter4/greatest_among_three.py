#def greatest(a,b,c):
   # if a>b and b>c:
    #    return a
    #elif b>c and c>a:
    #     return b
    #return c

    #one more method
def greater(a,b):
    if a>b:
        return a
    return b

def new_greatest(a,b,c):
    return greater(greater(a,b),c)

num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))
bigger=new_greatest(num1,num2,num3)
print(f"{bigger} is greatest among three")