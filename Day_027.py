from itertools import combinations

n = input("Enter list elements : ").split()
sub = [int(i) for i in n]
li= []
for i in range(1, len(sub)):   
    for sublist in set(combinations(sub, i)):
        if sum(sublist) == 0:
            li.append(sorted((list(sublist))))
if len(li)== 0 :
    print("No Zero Sublist found :-(")
else:
  print("Zero Sublist found :-)")
  for i in li:
    print(i)       