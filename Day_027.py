from itertools import combinations

n = input("Enter list elements : ").split()
sub = [int(i) for i in n]
negative = [ int(i) for i in n if int(i) < 0]
if len(negative)== 0:
    print("No Zero Sublist found :-(")
else:
  print("Zero Sublist found :-)")
  for i in range(1, len(sub)):   
    for sublist in set(combinations(sub, i)):
        if sum(sublist) == 0:
            print(sorted((list(sublist))))
        