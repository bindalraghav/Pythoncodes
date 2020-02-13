import random
winning_num=random.randint(1,100)
num=int(input("Guess a num 1-100 :"))
guess=0
game_over=False
while not game_over:
    if num== winning_num:
        print(f"You Win, and you guessed {guess} times")
        game_over=True
    else:
        if num <winning_num:
            print("Too Low")
            guess+=1
            num=int(input("Guess Again: "))
        else:
            print("Too High")
            guess+=1
            num=int(input("Guess Again: "))