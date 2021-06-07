// SOLUTION 1
// Validate Subsequence

// Complexity
// Average:  Time: | Space:
// Worst:    Time: | Space:

// O(n) time | O(1) space - where n is the length of the array
function isValidSubsequence(array, sequence) {
  let arrIdx = 0;
  let seqIdx = 0;

  const arrLen = array.length;
  const seqLen = sequence.length;

  while (arrIdx < arrLen && seqIdx < seqLen) {
    if (array[arrIdx] === sequence[seqIdx]) seqIdx++;
    arrIdx++;
  }
  return seqIdx === seqLen;
}
