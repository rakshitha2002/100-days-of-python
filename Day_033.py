# import permutation
from itertools import permutations
# input string
get_input = input("Enter string : ")
# find permutations
listing = ["".join(value) for value in permutations(get_input)]
# print output as alphabetical ordered permutations
print("\n".join(sorted(listing)))