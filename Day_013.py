def fibonacciNumberGenerator(N):
    """Your code here"""
    r =[0,1]
    if N == 1:
        return [r[0]]
    else:
        for i in range(2,N):
            num = r[-1]+r[-2]
            r.append(num)
        return r
# Make use of this main code to check manual test cases....
if __name__ == "__main__":
    N = int(input("Enter limit : "))
    print(fibonacciNumberGenerator(N))