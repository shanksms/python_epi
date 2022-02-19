from typing import Optional

from linkedlist_algorithms.linkedlist import ListNode


def check_cycle(head: Optional[ListNode]) -> bool:
    if not head:
        return False
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

