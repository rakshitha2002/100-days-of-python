list1 = int(input("Enter number of elements in first list : "))
l1 = [int(input(f"Enter {i} element of list : "))for i in range(1,list1+1)]
list2 = int(input("Enter number of elements in second list : "))
if list1 == list2:
  l2 = [int(input(f"Enter {j} element of list : "))for j in range(1,list2+1)]
  merge = l1 + l2
  merge.sort(reverse= True)
  print(merge)
else:
    print("make sure both the arrays must be with the same size")