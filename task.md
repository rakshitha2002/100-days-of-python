# Day10 - Amicable Pair Check
```
let's consider 2 numbers A & B, first you need to generate the proper divisors of A, then sum it, then generate the proper divisors of B, then sum it, if A's sum of proper divisors equals to B and B's sum of proper divisors equals to A means we can call the pair of numbers as Amicable Pair. 

Eg: A=220 and B=284
They are amicable pair because 

the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110, of which the sum is 284;

the proper divisors of 284 are 1, 2, 4, 71 and 142, of which the sum is 220.
```
---
## TestCase 1:-
---
### Input:
```
Enter two numbers : 220 284
```
### Output:
```
220 & 284 are Amicable numbers
```

## TestCase 2:-
---
### Input:
```
Enter two numbers : 100 200
```
### Output:
```
100 & 200 are not Amicable numbers
```

## TestCase 3:-
---
### Input:
```
Enter two numbers : 1184 1210
```
### Output:
```
1184 & 1210 are Amicable numbers
```