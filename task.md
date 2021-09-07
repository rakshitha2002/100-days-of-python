# Day24 - Lambda, Map, Filter and Reduce

- Get elements of the list. 
- Perform square for all the elements using ```map()``` function and print the same.
- Filter only odd number from the squared list using ```filter()``` function and print the same.
- Find product of all element of odd list using ```reduce()``` function and print the same.

---
## TestCase 1:-
---
### Input:
```
Enter number of elements in list : 3
Enter list elements : 3 2 1 
```
### Output:
```
Given list : [3, 2, 1]
Result after map() -> [9, 4, 1]
Result after filter() -> [9, 1]
Result after reduce() -> 9
```

## TestCase 2:-
---
### Input:
```
Enter number of elements in list : 5
Enter list elements : 9 79 63 52 51
```
### Output:
```
Given list : [9, 79, 63, 52, 51]
Result after map() -> [81, 6241, 3969, 2704, 2601]
Result after filter() -> [81, 6241, 3969, 2601]
Result after reduce() -> 5218679820249
```

## TestCase 3:-
---
### Input:
```
Enter number of elements in list : 5
Enter list elements : 58 56 52 54 55
```
### Output:
```
Given list : [58, 56, 52, 54, 55]
Result after map() -> [3364, 3136, 2704, 2916, 3025]
Result after filter() -> [3025]
Result after reduce() -> 3025
```