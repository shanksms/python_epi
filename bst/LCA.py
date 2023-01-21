
"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node
 in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/


"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Algorithm:
        1. if p.val <= root.val <= q.val, return root
        2. if root.val > p.val and root.val > q.val, move left
        3. if root.val < p.val and root.val < q.val, move right
        """
        if p.val > q.val:
            p, q = q, p
        if not root:
            return
        if p.val <= root.val <= q.val:
            return root
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)