from typing import Optional

from linkedlist_algorithms.linkedlist import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result
        while  list1  or  list2:
            if  list1 and  list2:
                if list1.data > list2.data:
                    current.next = ListNode(list2.data)
                    list2 = list2.next
                else:
                    current.next = ListNode(list1.data)
                    list1 = list1.next
            elif list1:
                current.next = ListNode(list1.data)
                list1 = list1.next
            else:
                current.next = ListNode(list2.data)
                list2 = list2.next
            current = current.next
        return result.next

if __name__ == '__main__':
    list1 = None
    list2 = ListNode(0, None)
    print(Solution().mergeTwoLists(list1, list2))
