"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
input
1 -> 2 -> 3 -> 4 -> 5

output
5 -> 4 -> 3 -> 2 -> 1

"""
from typing import Optional

from linkedlist_algorithms.linkedlist import ListNode


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    previous = None
    current = head
    _next = head.next
    while current:
        current.next = previous
        previous, current = current, _next
        if _next:
            _next = _next.next
    return previous


if __name__ == '__main__':
    head = ListNode(1, ListNode(2))
    rev = reverse_list(head)
    assert rev.data == 2 and rev.next.data == 1