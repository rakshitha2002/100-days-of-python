s = input("Enter string : ")
d = input("Enter character : ")
# convert string to list
l = [i for i in s]
# find the index of the character using len
v = [j for j in range(len(l)) if l[j] == d]
# print if character is present or not
if len(v) == 0:
    print(f"The character '{d}' not found")
else:
    print(f"The character '{d}' founded at {str(v)[1:-1]} index(es)")