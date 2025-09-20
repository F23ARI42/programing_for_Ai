todo=[]
def view(file_name):
    with open(file_name,"r") as file:
        my_file=file.read().splitlines()
        print(my_file)
def add(file_name, text):
    text=f"[] {text}"
    with open(file_name,"a") as file:
        file.write(text+"\n")
    todo.append(text.splitlines())
def complete(my_file,task_number):
    with open(my_file,"r") as file:
        task=file.readlines()
    task[task_number-1]=task[task_number-1].replace("[]", "[x]", 1)
    with open(my_file,"w") as file:
        file.writelines(task)
#add("file.txt", "workout")
# complete("file.txt",0)
# view("file.txt")
while True:
    user=input("Welcome to Todo List \nWhat do you want to do? \n1. Add \n2. View List \n3. Mark Complete \nEnter choice:")
    if user=="add" or user=="1":
        add_task=input("Enter Task: ")
        add("file.txt", add_task)
        print("Task added. enter Y to keep adding else stop")
    elif user == "view" or user == "2":
        view("file.txt")
    elif user == "mark complete" or user == "3":
        task_num = int(input("Enter Task Number: "))
        complete("file.txt", task_num)
    else:
        print("invalid inpnut")
        break



