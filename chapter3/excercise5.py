#Ask user to enter the name and print the no of time that alphabet occurs in the name
name=input("Enter full name: ")
i=0
temp= ""
while i<len(name):
    if name[i] not in temp:
        temp+=name[i]
        print(f"{name[i]}:{name.count(name[i])}")
    i=i+1
