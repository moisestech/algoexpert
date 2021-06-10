// resolve TypeScript error - Cannot redeclare block-scoped variable.
export {};

// SOLUTION 1
// Two Number Sum

// Complexity
// Average:  Time: | Space:
// Worst:    Time: | Space:

// Complexity: O(n^2) time | O(1) space

export function twoNumberSum(array: number[], targetSum: number) {
  for (let i = 0; i < array.length - 1; i++) {
    const firstNum = array[i];

    for (let j = i + 1; j < array.length; j++) {
      const secondNum = array[j];
      if (firstNum + secondNum === targetSum) {
        return [firstNum, secondNum];
      }
    }
  }
  return [];
}
