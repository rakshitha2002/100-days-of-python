def isSentencePalindrome(sentence):
    # Start coding after this line....
    lower_case = sentence.lower()
    without_space = "".join(i for i in lower_case if i.isalnum())
    if without_space[::1] == without_space[::-1]:
        return "Given string is a palindrome :-)"
    else:
        return "Given string is not a palindrome :-("
