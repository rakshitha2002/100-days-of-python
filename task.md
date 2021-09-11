# Day27 - Zero Sum Subarray/Sublist

- Get the list as the input
- Which contain +ve and -ve integer
- Find all sublist which sum is 0
> Note : Please import combinations from itertools for easy approach
---
## TestCase 1:-
---
### Input :-
```
Enter list elements : 9 -3 -3 -1 1 2 2 -4
```
### Output :-
```
Zero Sublist found :-)
[-1, 1]
[-3, 1, 2]
[-4, 2, 2]
[-3, -1, 2, 2]
[-4, -3, -3, 1, 9]
[-4, -1, 1, 2, 2]
[-4, -3, -3, -1, 2, 9]
```
---
## TestCase 2:-
---
### Input :-
```
Enter list elements : 5 -5 -1 1
```
### Output :-
```
Zero Sublist found :-)
[-5, 5]
[-1, 1]
```
---
## TestCase 3:-
---
### Input :-
```
Enter list elements : 5 5 7 6 2
```
### Output :-
```
No Zero Sublist found :-(
```