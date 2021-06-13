# Two Number Sum

[**Link**](https://www.algoexpert.io/questions/Two%20Number%20Sum)
Difficulty: Easy 🟢
Category:

---

## Problem

- Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
- If any two number in the input array sum, the function should return an empty array.
- **Note** that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.
- You can assumes that there will be at most one pair of number summing up to the target sum.

---

## Sample

### Input

```python
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
```

### Output

```python
[-1, 11] # the numbers could be in reverse order
```

---

## **Hints**

1. Try using two for loops to sum all possible pairs of number in the input array. What are the time and space implications of this approach?

2. Realize that for every number X in the input array, you are essentially trying to find a corresponding number Y such that X + Y = targetSum. With two variable in this equation known to you, it shouldn't be hard to solve for Y.

3. Try storing every number in a hash table, solving the equation mentioned in **Hint #2** for every number, and checking if the Y that you find is stored in the hash table. What are the time and space implications of this approach?

---

## Solution 1

- [JavaScript](./solution_1/two-number-sum.js)
- [TypeScript](./solution_1/two-number-sum.ts)
- [Python](./solution_1/two-number-sum.py)

## Solution 2

- [JavaScript]()
- [TypeScript]()
- [Python]()

---

## Optimal Time & Space Complexity

**Time:** `O(n)`  
**Space:** `O(n)`

Where **n** is the length of the input array.

<img src="../../assets/big-o-complexity-chart.jpg" style="width: 600px"/>
