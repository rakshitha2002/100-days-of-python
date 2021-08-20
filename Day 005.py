a = float(input("Enter side a length : "))
b = float(input("Enter side b length : "))
c = float(input("Enter side c length : ")) 
print("Area of Triangle : ",(((a + b + c) / 2)*(((a + b + c) / 2) - a)*(((a + b + c) / 2) - b)*(((a + b + c) / 2) - c)) ** 0.5)