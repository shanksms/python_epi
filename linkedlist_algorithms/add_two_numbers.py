"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return
the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
2 -> 4 -> 3
5 -> 6 -> 4

243 + 564 = 708
7 -> 0-> 8

"""
from typing import Optional

from linkedlist_algorithms.linkedlist import ListNode


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    current1 = l1
    current2 = l2
    carry = 0
    head = current = ListNode(0)
    while current1 or current2:
        _sum = (current1.val if current1 else 0) + (current2.val if current2 else 0) + carry
        div, mod = divmod(_sum, 10)
        n = ListNode(mod)
        carry = div
        current.next = n
        current = current.next
        if current1:
            current1 = current1.next
        if current2:
            current2 = current2.next

    if carry:
        current.next = ListNode(carry)

    return head.next