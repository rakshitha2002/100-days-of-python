n = int(input("Enter number of elements in list : "))
l=[int(input(f"Enter {i} element of list : ")) for i in range(1,n+1)]
print("Given list elements : ",l)
element = int(input("Enter the element to be searched (first occurrence) : "))
print(f"Element {element} found at index {l.index(element)}")
print(f"Sorted list elements : {sorted(l)}")
for j in sorted(set(l)):
    print(f"{j} occurs {l.count(j)} time(s)")