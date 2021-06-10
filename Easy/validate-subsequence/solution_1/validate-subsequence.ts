// resolve TypeScript error - Cannot redeclare block-scoped variable.
export {};

// SOLUTION 1
// Validate Subsequence

// Complexity
// Average:  Time: | Space:
// Worst:    Time: | Space:

// O(n) time | O(1) space

export function isValidSubsequence(array: number[], sequence: number[]) {
  let arrIdx = 0;
  let seqIdx = 0;

  while (arrIdx < array.length && seqIdx < sequence.length) {
    if (array[arrIdx] === sequence[seqIdx]) seqIdx++;
    arrIdx++;
  }
  return seqIdx === sequence.length;
}
