# problem
# ask user to input a number containing more than one digit
# example - 1256
# calculate 1+2+5+6 and print

num=input("Enter any no. more then 1 digit")
sum=0
i=0
while i<len(num):
    sum=sum+int(num[i])
    i=i+1
print(sum)