"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.



Example 1:
     3
    /
9       20
    /      \
   15       7
Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
from binary_tree_algorithms.binary_tree_node import BinaryTreeNode


def max_depth(root: BinaryTreeNode) -> int:
    '''
    Algorithm:
    1. for each note, find the depth of left child and right child.
    2. take the max depth from step 1 + 1
    3. return 0 if node is None
    :param root:
    :return:
    '''
    if root is None:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return max(left_depth, right_depth) + 1
