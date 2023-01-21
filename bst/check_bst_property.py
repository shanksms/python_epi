"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:
    2
1       3

Below is not a valid BST since 6 is more than 5 even it lies on the right side of the root (5)

    5
1       7
    6       8



"""
import math
from typing import Optional

from bst.bst import TreeNode

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
          Algorithm
          min = -math.inf and max = math.max
          we want to make root is always passing the condition. Hence we kept min and max what we kept.
          1. At each level, the value should be in between max and min.
          2. recurse left and pass currentlevel.val as max, min as min
          3. recurse right and pass max as max, currentlevel.val as min
          Key idea here is, that when you in case of left most nodes, you only need check their max value since they can
          take any minimum value. Similarly for right most nodes, you only need to worry about their min value
          since they can take any max value.
          :param root:
          :return:
          """
        if not root:
            return True
        max_val = min_val = root.val
        return self.helper(root.left, -math.inf, max_val) and self.helper(root.right, min_val, math.inf)

    def helper(self, root, min_val, max_val):
        if not root:
            return True
        if root.val <= min_val:
            return False
        if root.val >= max_val:
            return False
        return self.helper(root.left, min_val, root.val) and self.helper(root.right, root.val, max_val)