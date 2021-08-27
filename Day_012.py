def isVowel(letter):
    """Your code here"""
    if letter in ('a','A','e','E','i','I','o','O','u','U'):
        return True
    else:
        return False
    
# Make use of this main code to check manual test cases....
if __name__ == "__main__":
    letter = input("Enter letter : ")
    print(isVowel(letter))