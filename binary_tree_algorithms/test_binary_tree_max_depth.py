import pytest
from binary_tree_algorithms import binary_tree_max_depth
from binary_tree_algorithms.binary_tree_node import BinaryTreeNode


def test_max_depth():
    left = BinaryTreeNode(9, None, None)
    right = BinaryTreeNode(20, BinaryTreeNode(15, None, None), BinaryTreeNode(7, None, None))
    root = BinaryTreeNode(3, left, right)
    assert binary_tree_max_depth.max_depth(root) == 3