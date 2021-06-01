// SOLUTION 1
// Sorted Squared Array
// Complexity: O(n log n) time | O(n) - where n is the length of the input array

function sortedSquaredArray(array) {
  const arrLen = array.length;
  const sortedSquares = new Array(arrLen).fill(0);

  for (let idx = 0; idx < arrLen; idx++) {
    const value = array[idx];
    sortedSquares[idx] = value ** 2;
  }

  sortedSquares.sort((a, b) => a - b);
  return sortedSquares;
}
