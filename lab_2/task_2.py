pizza=input("please enter your pizza size :")
if pizza=="small":
    price=15
elif pizza=="medium":
    price=20
elif pizza=="large":
    price=25
else:
    print("please enter a valid pizza size")
if pizza!="small" and pizza!="medium" and pizza!="large":
    print("end")
else:
    extr_peprony=(input("please enter extr peprony yes/or no :"))
    if extr_peprony=="yes":
        if pizza=="small":
            price+=2
        elif pizza=="medium":
            price+=2.5
        elif pizza=="large":
            price+=3.5
        else:
            print("thank you")
    extra_cheese=(input("please enter extr cheese yes/or no :"))
    if extra_cheese=="yes":
        if pizza=="small":
            price+=1
        elif pizza=="medium":
            price+=2
        elif pizza=="large":
            price+=2.5
        else:
            print("thank you")
print(price)
