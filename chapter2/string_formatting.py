#string formatting

name=input("Enter your name ")
age=input("enter your age ")
#python 3 method
print("hey {} your age is {}".format(name,age))
#python 3.6
print(f"Hey{name} your age is{age}")

#string indexing
language="python"
print("string indexing eg as follows")
print(language[2])
print(language[-3])
#String Slicing
print("String slicing eg as follows")
print(language[1:4])
#Step argument
print("step argument-")
print(language[0::2])
#reverse of string
print("reverse-")
print("name in reverse ="+name[5::-1])