from typing import Optional

from linkedlist_algorithms.linkedlist import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_pos_dict = {}
        current = head
        pos = 0
        while current:
            if current in node_pos_dict:
                return current
            node_pos_dict[current] = pos
            pos += 1
            current = current.next
        return None