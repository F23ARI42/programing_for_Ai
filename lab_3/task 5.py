import random
print("enter your deficulty easy/hard")
deficity = input().strip().split()
screen_num=random.randint(1,100)
attemps=10 if deficity=="easy" else 5
while attemps>0:
        quess=int(input("guess number"))
        if quess==screen_num:
            print("you guessed right")
        elif quess>screen_num:
            print("you guessed too high")
        else:
            print("you guessed too low")
        attemps-=1
        if attemps >0:
                print(f"Guess again.\nYou have {attemps} attempts remaining to guess the number.")
        else:
            print("You've run out of guesses, you lose.")


