#print no. 1 to 10 but stop on 5
for i in range(1,11):
    if i==5:
        break
    print(i)

#print no. 1-10 except 5
for i in range(1,11):
    if i==5:
        continue
    print(i)