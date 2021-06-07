# Validate Subsequence

[**Link**](https://www.algoexpert.io/questions/Validate%20Subsequence)

- Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

---

## Sample

### Input

```python
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
```

### Output

```python
true
```

---

## Hints

1. You can solve this question by iterating through the main input array once.

2. Iterate through the main array, and look for the first integer in the potential subsequence. If you find that integer, keep on iterating through the main array, but now look for the second integer in the potential subsequence. Continue this process until you either find every integer in the potential subsequence or you reach the end of the main array.

3. To actually implement what **Hint #2** describes, you'll have to declare a variable holding your position in the potential subsequence. At first, this position will be the 0th index in the sequence; as you find the sequence's integers in the main array, you'll increment the position variable until you reach the end of the sequence.

---

## Optimal Space & Time Complexity

O(n) time | O(n) space - where n is the length of the input array.

**Solution 1**: O(n) time | O(1) space
**Solution 2**: O(n) time | O(1) space

---

## Solution 1

- [JavaScript]()
- [TypeScript]()
- [Python]()

## Solution 2

- [JavaScript]()
- [TypeScript]()
- [Python]()
