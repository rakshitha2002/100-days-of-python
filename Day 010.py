def sum(num):
    divisor = 0
    for i in range(1,num):
        if num % i == 0:
            divisor += i
    return divisor
n1,n2 = input("Enter two numbers : ").split()
if int(n2) == sum(int(n1)) and int(n1) == sum(int(n2)):
    print(f"{int(n1)} & {int(n2)} are Amicable numbers")
else :
    print(f"{int(n1)}& {int(n2)} are not Amicable numbers")

