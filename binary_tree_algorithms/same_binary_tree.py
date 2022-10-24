from binary_tree_algorithms.binary_tree_node import BinaryTreeNode


def is_same_tree(left: BinaryTreeNode, right: BinaryTreeNode) -> bool:
    if not left and not right:
        return True
    elif left and not right:
        return False
    elif not left and right:
        return False
    else:
        if left.val != right.val:
            return False
        else:
            return is_same_tree(left.left, right.left) and is_same_tree(left.right, right.right)
