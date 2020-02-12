#Q= user se comma seprate name input krvana or ek characther input krvana or jo character hai vo name m kitni baar aayavo batana
name,character=input("Enter name and character comma saprated ").split(",")
length=len(name)
name2=name.lower()
print(length)
character=character.lower()
print(name2.count(character))