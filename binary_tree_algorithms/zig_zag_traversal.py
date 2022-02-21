from collections import deque
from typing import Optional, List

from binary_tree_algorithms.binary_tree_node import BinaryTreeNode
"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right,
then right to left for the next level and alternate between).
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

 
"""

def zigzagLevelOrder(root: Optional[BinaryTreeNode]) -> List[List[int]]:
    result = []
    if not root:
        return result
    queue = deque()
    queue.appendleft(root)
    flip = False
    while len(queue) > 0:
        tmp_ls = []
        for _ in range(len(queue)):
            node = queue.pop()
            tmp_ls.append(node.val)
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)

        if flip:
            result.append(tmp_ls[::-1])
        else:
            result.append(tmp_ls)
        flip = not flip
    return result