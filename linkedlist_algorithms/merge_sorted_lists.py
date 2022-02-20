from typing import Optional, List
from linkedlist_algorithms.linkedlist import ListNode
import heapq


def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # second condition is to check empty sublists
    if not lists or not any(lists):
        return None
    min_heap = []
    for _idx, llist in enumerate(lists):
        if llist:
            heapq.heappush(min_heap, (llist.val, _idx))
            lists[_idx] = llist.next

    dummy_node = ListNode()
    tail = dummy_node
    while len(min_heap) > 0:
        val, _idx = heapq.heappop(min_heap)
        node = ListNode(val)
        tail.next, tail = node, node
        if lists[_idx]:
            heapq.heappush(min_heap, (lists[_idx].val, _idx))
            lists[_idx] = lists[_idx].next

    return dummy_node.next

