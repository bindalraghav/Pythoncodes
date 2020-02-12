#Sum from 1 to n

#n=input("Enter any num ")
#n=int(n)
#sum=0
#for n in range(1,n+1):
#    sum+=n
#print(sum)

#Sum of digits in number enter by user
#num=input("Enter any digit ")
#sum=0
#for i in range(len(num)):
    #sum+=int(num[i])
#print(sum)

#count of character in name
name=input("Enter full name ")
temp=""
for i in range(len(name)):
     if name[i] not in temp:
        temp+=name[i]
        print(f"{name[i]}:{name.count(name[i])}")