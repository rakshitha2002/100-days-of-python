n = input("Enter list elements : ").split()
sub = [int(i) for i in n]
output=[]
temp = []
for i in sub:
   if i == 0:
      output.append(temp)
      temp = []
      temp.append(i)
   if i == 1:
      output.append(temp)
      temp.append(i)
s = []     
for i in output:
   s.append(sum(i))  
print(f"Max one's in sublist : {max(s)}")