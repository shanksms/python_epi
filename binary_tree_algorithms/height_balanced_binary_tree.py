"""
in a Height balanced Binary Tree, difference of heights between left and right subtree is not more than 1
Algorithm:
1. At any level, find out height of left and right subtree and whether they are balanced or not.
2. if one of them is not height balanced, return False
3. Calculate difference of heights between the left and right subtree.
4. Return height and IsBalanced value
"""

from collections import namedtuple

from binary_tree_algorithms.binary_tree_node import BinaryTreeNode

BalancedHeightTree = namedtuple('BalancedHeightTree', ('isBalanced', 'height'))


def check_heights(root):
    if not root:
        return BalancedHeightTree(True, -1)
    # check left subtree height
    left = check_heights(root.left)
    if not left.isBalanced:
        return BalancedHeightTree(False, 0)
    right = check_heights(root.right)
    if not right.isBalanced:
        return BalancedHeightTree(False, 0)
    diff = abs(left.height - right.height)
    height = max(left.height, right.height) + 1
    isBalanced = True if diff <= 1 else False

    return BalancedHeightTree(isBalanced, height)


def check_height_balanced_tree(root):
    if not root:
        return False
    return check_heights(root).isBalanced


if __name__ == '__main__':
    left = BinaryTreeNode(2, None, None)
    right = BinaryTreeNode(3, None, None)
    root = BinaryTreeNode(1, left=left, right=right)
    print(check_height_balanced_tree(root))
