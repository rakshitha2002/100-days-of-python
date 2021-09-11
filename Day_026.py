loop = True
def sums(n):
    while len(n)!=1:
       su = 0
       for i in n: 
          su+= int(i)
       n = str(su)
    return n
def integer():
    n = input("Enter integer value : ")
    sums(n) 
    print(f"Sum of integer digits : {sums(n)}")    
def string():
    k = input("Enter string value : ")
    d =  k.lower()
    numbers = sum([ord(i)- 96 for i in d])
    sums(str(numbers))
    print(f"Sum of string digits : {sums(str(numbers))}")
def exit():
    global loop
    loop = False
while loop:
    print("\nSelect input type: \n1. Integer \n2. String \n3. Exit ")
    choice = int(input())
    if choice == 1:
        integer()
    elif choice == 2:
        string()
    elif choice == 3:
        exit()         