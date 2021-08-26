N= int(input("Enter a positive integer : "))
l = [int(input(f"Enter Input {i} number : "))for i in range(1,N+1)]
print(f"The sum of {N} no is : {sum(l)}")
print(f"The average of {N} no is : {round(sum(l) / len(l),2)}")