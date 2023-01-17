from typing import Optional

from linkedlist_algorithms.linkedlist import ListNode


"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 
"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. start n1 and n2
        2. n1 will move one step, n2 will move two steps
        3. when n2 reaches end, break the loop.
        """

        slow_node = fast_node = head
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

        return slow_node
