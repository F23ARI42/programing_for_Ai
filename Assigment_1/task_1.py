num=int(input("enter you height"))
height=[]
for i in range(num):
    element=float(input(f"enter a height{i+1}"))
    height.append(element)
    average=(element)/num
print(average)

