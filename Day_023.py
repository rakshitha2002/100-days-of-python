l = []
loop = True
def Insert():
    li = input("Enter new list elements : ").split()
    for i in li:
       l.append(i)
def Delete():
    if len(l) > 0 :
        Display()
        delete = int(input("\nEnter element index to delete : "))
        l.pop(delete)
    else:
        print("Please insert elements to perform delete operation")
def Display():
    if len(l)!=0:
       print("List elements are : ")
       for i in l:
           print(f"{i}({l.index(i)})",end = " ")
    else:
        print("Nothing to display list is empty!")
def Exit():
    Display()
    print("Bye see you soon !")
    global loop
    loop = False

while loop:
    print("\nWhat do you want to do \n1. Insert \n2. Delete \n3. Display \n4. Exit ")
    choice = int(input())
    if choice == 1:
        Insert()
    elif choice == 2:
        Delete()
    elif choice == 3:
        Display()
    elif choice == 4:
        Exit()
        
   