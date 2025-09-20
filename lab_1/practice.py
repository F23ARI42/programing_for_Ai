amount=int(input("enter amount"))
if amount > 5000:
    total=amount*0.15
    print("your amont is with discount 15%",total)
    print("your amont is with discount",amount-total)
else:
    print("sorry no discount")
