s = input("Enter string : ")
l =[ i for i in s if i in "aeiouAEIOU"]
if len(l) >=1:
    n =[ord(i) for i in l]
    print(f"The vowel(s) is(are) {str(l)[1:-1]}\nASCII summation is {sum(n)}")
else:
    print("Given word don't have any vowel, hence ASCII summation is 0")