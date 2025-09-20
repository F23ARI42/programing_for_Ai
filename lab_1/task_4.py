print("welocme to the tip calculator")
total_bill =float(input("Enter the total bill: "))
tip=int(input("Enter the tip amount: "))
people = int(input("Enter the number of people: "))
total= total_bill+tip
divide=total/people
print("The total bill is:",divide.__round__())
