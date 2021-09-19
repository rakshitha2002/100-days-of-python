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
    for i in sorted(set(k)):
        if k.count(i)>1:
            print(f"letter '{i}' occurs {k.count(i)} time(s)")
        else:
            print("All the letters occurs exactly once")
            break
        