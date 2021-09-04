x = int(input("Enter number : "))
for j in range(x,0,-1):
    print(" * "* j +  "   "*(x-j) + "   "*(x-j) + " * "* j)  
for i in range(1,x+1):
    print(" * "* i +  "   "*(x-i) + "   "*(x-i) + " * "* i)