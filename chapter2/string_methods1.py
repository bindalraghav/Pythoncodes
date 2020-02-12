name="   Raghav BIndal   "
#len()func-ye characters ko  count karega
print(len(name))
#lower()method- ye puri string ko lower case mai chng krdega
print(name.lower())
#upper()method-upr case mai convert krega
print(name.upper())
#title()-ye frst letter ko upper mai or sbko lower mai krdega
print(name.title())
#count()- ye count krega vo character jo hum puchege
print(name.count("a"))
#strip method - spaces khtm krne k liye
print(name.strip())
#replace method
string="i love you but u dont love me"
print(string.replace(" ","_"))
#find method
print(string.find("love"))
#what if i want to find position of 2 love?
love_pos1=string.find("love")
love_pos2=string.find("love",love_pos1+1)
print(love_pos2)

