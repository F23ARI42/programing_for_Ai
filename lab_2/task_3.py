name=input("plese your name")
name1=input("plese your name")
combinet=name+name1
cout_t=combinet.count("t")
cout_r=combinet.count("r")
count_u=combinet.count("u")
count_e=combinet.count("e")
true=cout_t+cout_r+count_u+count_e
print(true)
count_l=combinet.count("l")
count_o=combinet.count("o")
count_v=combinet.count("v")
count_e=combinet.count("e")
love=count_l+count_o+count_v+count_e
print(love)
total=int(f"{true}{love}")
if total>40 and total<50:
    print("you are living togher")
else:
    print(total)
