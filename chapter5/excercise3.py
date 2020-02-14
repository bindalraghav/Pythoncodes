#REVERSE OF EACH STRING IN LIST
def reversestring(string):
    elements=[]
    for i in string:
        elements.append(i[::-1])
    return elements

names=['Raghav','Divyansh','Bhattu']
print(reversestring(names))
    