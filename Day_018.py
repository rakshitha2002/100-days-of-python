n = int(input("Enter odd number : "))
median = (n+1)/2
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == median and j == median :
            print("0",end ="  ")
        else:
            print("#",end ="  ")
    print()