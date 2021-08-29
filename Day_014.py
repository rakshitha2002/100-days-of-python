def isPrimeNumber(number):
    """ Check given number is prime number """
    factor = 0
    for i in range(2,number):
        if(number % i == 0):
            factor = i
    if factor > 1:
        return False
    else:
        return True
def isFibonacciNumber(number):
    """ Check given number is fibonacci """
    r =[0,1]
    for i in range(2,number+1):
        num = r[-1]+r[-2]
        r.append(num)
    if number in r:
        return True
    else:
        return False
def isprimeFibonacciNumber(N):
    """ Check given N is prime and fibonacci number """
    if isPrimeNumber(N)  and isFibonacciNumber(N)  :
        return True , f"isPrimeNumber : {isPrimeNumber(N)} & isFibonacciNumber : {isFibonacciNumber(N)}"
    else:
        return False , f"isPrimeNumber : {isPrimeNumber(N)} & isFibonacciNumber : {isFibonacciNumber(N)}"
# Make use of this main code to check manual test cases....
if __name__ == "__main__":
    N = int(input("Enter number : "))
    print(isprimeFibonacciNumber(N))