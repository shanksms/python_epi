from binary_tree_algorithms.binary_tree_node import BinaryTreeNode


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



if __name__ == '__main__':
    left = BinaryTreeNode(2, None, None)
    right = BinaryTreeNode(3, None, None)
    root = BinaryTreeNode(1, left=left, right=right)
    print('#'* 80)
    print('in order')
    in_order(root)
    print('#' * 80)
    print('pre order')
    pre_order(root)
    print('#' * 80)
    print('post order')
    post_order(root)
