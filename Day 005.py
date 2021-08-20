a = float(input("Enter side a length : "))
b = float(input("Enter side b length : "))
c = float(input("Enter side c length : ")) 
s = (a + b + c) / 2
print("Area of Triangle : ",(s * (s - a) * (s - b) * (s - c)) ** 0.5)