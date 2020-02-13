#greater of two num
def greater(a,b):
    if a>b:
        return a
    return b

num1=int(input("enter first num:"))
num2=int(input("Enter second num:"))
bigger=greater(num1,num2)
print(f"{bigger} is greater")