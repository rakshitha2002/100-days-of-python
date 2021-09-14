n = input("Enter list elements : ").split()
sub = [int(i) for i in n]
output=[]
temp = []
for i in sub:
   if len(temp)!=0:
      if temp[-1]== i:
         temp.append(i)
      else:
         output.append(temp)
         temp = []
         temp.append(i)
   else:
      temp.append(i)
output.append(temp)
s = [ sum(i) for i in output]     
print(f"Max one's in sublist : {max(s)}")