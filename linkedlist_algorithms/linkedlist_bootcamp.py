from linkedlist_algorithms.linkedlist import ListNode


def search_node(root, node_to_find):
    while root != None and root != node_to_find:
        root = root.next
    return root




if __name__ == "__main__":
    child = ListNode(2, None)
    root = ListNode(1, child)
    print(search_node(root, child))
