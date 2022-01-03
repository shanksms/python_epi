from binary_tree_algorithms.binary_tree_node import BinaryTreeNode
from binary_tree_algorithms.symmetric_binary_tree import symmetric

def test_symmetric():
    left = BinaryTreeNode(2, left=None, right=None)
    right = BinaryTreeNode(2, left=None, right=None)
    root = BinaryTreeNode(1, left=left, right=right)
    assert symmetric(root)

