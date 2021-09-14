# Day29 - String Processing-I

- Get a string as input.  
- Find whether given string contains consecutive letters and each letter occurs exactly once.  
- Get the sequence of alphabets through console.  
- Be specific with the output format, refer all the Sample Inputs and Sample Outputs for more clarity.  
---
## Explanation :-
```
input string : dcab
dcab -> abcd -> This word is consecutive letter.  
input string : xyba
xyba -> abxy  -> This word is not consecutive letter.
```
---
## TestCase 1:-
---
### Input :-
```
Enter string : dcab
```
### Output :-
```
The string 'a','b','c','d' which are consecutive letters
All the letters occurs exactly once
```
---
## TestCase 2:-
---
### Input :-
```
Enter string : xyba
```
### Output :-
```
The string 'x','y','b','a' which are not consecutive letters
All the letters occurs exactly once
```
---
## TestCase 3:-
---
### Input :-
```
Enter string : pppqrstppppqrst
```
### Output :-
```
The string 'p','p','p','q','r','s','t','p','p','p','p','q','r','s','t' which are not consecutive letters
letter 'p' occurs 7 time(s)
letter 'q' occurs 2 time(s)
letter 'r' occurs 2 time(s)
letter 's' occurs 2 time(s)
letter 't' occurs 2 time(s)
```