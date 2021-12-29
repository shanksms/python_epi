from collections import deque

from binary_tree_algorithms.binary_tree_node import BinaryTreeNode
from typing import List


def in_order(root: BinaryTreeNode):
    if root:
        in_order(root.left)
        print(root.data)
        in_order(root.right)


def pre_order(root: BinaryTreeNode):
    if root:
        print(root.data)
        in_order(root.left)
        in_order(root.right)


def post_order(root: BinaryTreeNode):
    if root:
        in_order(root.left)
        in_order(root.right)
        print(root.data)


def level_order_traversal(root: BinaryTreeNode) -> List:
    result = []
    if not root:
        return result
    queue = deque()
    queue.appendleft(root)
    while len(queue) != 0:
        node = queue.pop()
        if node.left:
            queue.appendleft(node.left)
        if node.right:
            queue.appendleft(node.right)
        result.append(node.data)
    return result


if __name__ == '__main__':
    left = BinaryTreeNode(2, None, None)
    right = BinaryTreeNode(3, None, None)
    root = BinaryTreeNode(1, left=left, right=right)
    print('#' * 80)
    print('in order')
    in_order(root)
    print('#' * 80)
    print('pre order')
    pre_order(root)
    print('#' * 80)
    print('post order')
    post_order(root)
    print('#' * 80)
    print('level order')
    print(level_order_traversal(root))
