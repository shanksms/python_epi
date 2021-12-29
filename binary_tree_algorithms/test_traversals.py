from binary_tree_algorithms.traversals import level_order_traversal
from binary_tree_algorithms.binary_tree_node import BinaryTreeNode

def test_level_order_traversal():
    n1 = BinaryTreeNode(4, None, None)
    n2 = BinaryTreeNode(5, None, None)
    n3 = BinaryTreeNode(2, left=n1, right=n2)
    n4 = BinaryTreeNode(6, None, None)
    n5 = BinaryTreeNode(7, None, None)
    n6 = BinaryTreeNode(3, left=n4, right=n5)
    root = BinaryTreeNode(1, left=n3, right=n6)
    expected_result = [1, 2, 3, 4, 5, 6, 7]
    assert level_order_traversal(root) == expected_result



