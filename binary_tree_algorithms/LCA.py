from binary_tree_algorithms.binary_tree_node import BinaryTreeNode


def lca(root: BinaryTreeNode, node1: BinaryTreeNode, node2: BinaryTreeNode):
    if not root or root == node1 or root == node2:
        return root
    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    if left and right:
        return root
    return left if left else right


if __name__ == '__main__':
    left = BinaryTreeNode(2, None, None)
    right = BinaryTreeNode(3, None, None)
    root = BinaryTreeNode(1, left, right)
    assert root.data == lca(root, left, right).data
