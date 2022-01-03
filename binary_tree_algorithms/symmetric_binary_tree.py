from binary_tree_algorithms.binary_tree_node import BinaryTreeNode


def symmetric(root: BinaryTreeNode):
    if not root:
        return True
    def solve(left: BinaryTreeNode, right: BinaryTreeNode):
        if not left and not right:
            return True
        if not left or not right:
            # one of the child or right is None
            return False
        if left.data == right.data:
            return solve(left.left, right.right)

    return solve(root.left, root.right)

