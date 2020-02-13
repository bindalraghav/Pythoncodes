def its_pallidrome(name):
    if name==name[::-1]:
        return True
    return False

names=input("Enter any name ")
print(its_pallidrome(names))
