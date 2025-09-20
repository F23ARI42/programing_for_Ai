
def bid():
    user ={}
    key=int(input("enter your amount"))
    value=input("enter you enter your name ")
    other_bidder=input("enter your other bidder yes/no")
    user[key]=value
    if other_bidder=="yes":
        bid()
    else:
        if other_bidder=="no":
            winner=max(user.keys())
            total=user[winner]
            print("this bid winner is ",winner,total)
bid()


