#first read thw file
with open("input/letter/starting_letter.txt", "r") as f:
   letter=f.read()
   #print(letter)
with open("input/names/names.txt", "r") as f:
    names=f.read().splitlines()
    #print(names)
for name in names:
    each_name=letter.replace("[name]", name)
    with open(f"output/invitation/{name}.txt", "w") as f:
        f.write(each_name)
