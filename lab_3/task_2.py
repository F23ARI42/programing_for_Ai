
def primen(num):
    if num==1:
        print("prime number is greater than one")
    i=2
    while i*i<=num:
        if num%i==0:
            return False
        i+=1
        return True
num=int(input("enter you num"))
if primen(num):
    print("prime number ")
else:
    print("not prime")

