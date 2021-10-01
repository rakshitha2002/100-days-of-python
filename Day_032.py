#get the input
f = input("Enter string : ")
#check alphanumeric and if space also joined
h = "".join(i for i in f if i.isalnum() or i == " ")
#split the string and join the spaces and print the output
print("Final result : "+" ".join(h.split()))