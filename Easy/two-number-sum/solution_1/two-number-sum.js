// SOLUTION 1
// Two Number Sum
// Complexity: O(n^2) time | O(1) space

function twoNumberSum(array, targetSum) {
  const arrLen = array.length;
  for (let i = 0; i < arrLen - 1; i++) {
    const firstNum = array[i];
    for (let j = i + 1; j < arrLen; j++) {
      const secondNum = array[j];
      if (firstNum + secondNum === targetSum) {
        return [firstNum, secondNum];
      }
    }
  }
  return [];
}
