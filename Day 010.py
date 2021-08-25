n1,n2 = input("Enter two numbers : ").split()
num1 = int(n1)
num2 = int(n2)
divisor = 0
divisor2 = 0
for i in range(1,num1):
    if num1 % i == 0:
        divisor += i
for j in range(1,num2):
    if num2 % j == 0:
        divisor2 += j
if num1 == divisor2 and num2 == divisor :
    print(f"{num1} & {num2} are Amicable numbers")
else :
    print(f"{num1} & {num2} are not Amicable numbers")
