# Day26 - Sum of digits/letter

- Create menu for select input type.
1. Integer
    - Get an integer value as input and perform recursive sum of same.
> Example : 18767986 -> 1 + 8 + 7 + 6 + 7 + 9 + 8 + 6 = 52 -> 5 + 2 = 7.
2. String
    - Get an string value as input and  perform recursive sum of same.
    - Please do convert string values to lower case.
    - Substitute number equivalent for alphabets to find sum, 1 for a, 2 for b,…,26 for z.
> Example : PythOn -> python -> 16 + 25 + 20 + 8 + 15 + 14 = 98 -> 9 + 8 = 17 -> 1 + 7 = 8.

---
## TestCase 1:-
---
```
Select input type:
1. Integer        
2. String
3. Exit
1
Enter integer value : 18767986
Sum of integer digits : 7

Select input type:
1. Integer
2. String
3. Exit
2
Enter string value : PythOn
Sum of string digits : 8

Select input type:
1. Integer
2. String
3. Exit
3
```

## TestCase 2:-
---
```
Select input type:
1. Integer        
2. String
3. Exit
2
Enter string value : Coding
Sum of string digits : 7

Select input type:
1. Integer
2. String
3. Exit
1
Enter integer value : 8756924518295955646519289988918
Sum of integer digits : 3

Select input type:
1. Integer
2. String
3. Exit
3
```
