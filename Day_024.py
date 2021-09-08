from functools import reduce
elements = int(input("Enter number of elements in list : "))
l = [ int(i)for i in input("Enter list elements : ").split()]
print(f"Given list : {l}")
square = list(map(lambda a : a*a,l))
print(f"Result after map() -> {square}")
odd = list(filter(lambda n : n if n% 2!= 0 else None,square))
print(f"Result after filter() -> {odd}")
print(f"Result after reduce() -> {reduce((lambda  j,k: j*k),odd)}")