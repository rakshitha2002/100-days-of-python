s = input("Enter string : ")
m=[i for i in s]
k = sorted(m)
is_consecutive_flag=True
for i in range(0,len(k)-1):
    if ord(k[i]) != ord(k[i+1])-1:
        is_consecutive_flag=False
        break
if is_consecutive_flag: 
    print(f"The string {str(k)[1:-1]} which are consecutive letters") 
    print("All the letters occurs exactly once")
else:
    print(f"The string {str(k)[1:-1]} which are not consecutive letters")
    is_value_flag = True
    for i in sorted(set(k)):
        if k.count(i)!=1:
            is_value_flag=False
            break
    if is_value_flag:
          print("All the letters occurs exactly once")
    else:
        for i in sorted(set(k)): 
           print(f"letter {i} occur {k.count(i)}time(s)")       