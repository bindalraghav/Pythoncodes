winning_num=27
user_num=input("Enter the num between 1-100: ")
user_num=int(user_num)
if user_num==winning_num:
    print("YOU WIN!!!")
else:
    if user_num<winning_num:
        print("TOO LOW..")
    else:
        print("TOO HIGH..")