from typing import List
"""
https://leetcode.com/problems/n-ary-tree-preorder-traversal/
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: Node) -> List[int]:
        ls = []
        self.helper(root, ls)
        return ls

    def helper(self, root, ls):
        if not root:
            return
        ls.append(root.val)
        for child in root.children:
            self.helper(child, ls)
