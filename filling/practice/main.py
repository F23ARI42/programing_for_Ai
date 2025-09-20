word="learning"
with open("prctice.txt", "r") as file:
    data=file.read()
    if (data.find(word) !=-1):
        print("found")
    else:
        print("not found")

