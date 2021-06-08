// resolve TypeScript error - Cannot redeclare block-scoped variable.
export {};

// SOLUTION 1
// Node Depths

// Complexity
// Average: when the tree is balanced
// 	Time: O(n)  | n is the number of nodes in the Binary Tree
// 	Space: O(h)	| h is the height of the Binary Tree
// Worst: when the tree is not balanced

export function nodeDepths(root: BinaryTree) {
  // Write your code here.
  return -1;
}

// This is the class of the input binary tree.
class BinaryTree {
  value: number;
  left: BinaryTree | null;
  right: BinaryTree | null;

  constructor(value: number) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}
