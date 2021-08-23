number = int(input("Enter a positive integer : "))
factor = 0
if number == 1:
    print("1 is neither a prime nor a composite number.")
else:
    for i in range(2,number):
        if(number % i == 0):
             factor = i
    if factor > 1:
        print(f"{number} is not a prime number.")
    else:
        print(f"{number} is a prime number.")