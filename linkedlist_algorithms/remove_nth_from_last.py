"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
1 -> 2 -> 3 -> 4 -> 5
n  = 2
output: 1 -> 2 -> 3 -> 5

Example 2:
1
n = 1
output: [] or None

"""
from typing import Optional

from linkedlist_algorithms.linkedlist import ListNode


def removeNthFromEnd( head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # dummy node is created to handle the case where we remove the head of the linked list itself.
    dummy = ListNode(0, head)

    ptr1 = ptr2 = dummy
    for _ in range(n + 1):
        ptr1 = ptr1.next
    while ptr1:
        ptr2 = ptr2.next
        ptr1 = ptr1.next
    ptr2.next = ptr2.next.next

    return dummy.next