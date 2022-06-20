"""
Given a non-negative integer represented as a linked list of digits, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list.



Example 1:

Input: head = [1,2,3]
Output: [1,2,4]
Example 2:

Input: head = [0]
Output: [1]
"""
from linkedlist_algorithms.linkedlist import ListNode


def plusOne_approach1(head: ListNode) -> ListNode:
    temp_ls = []
    curr_node = head
    while curr_node:
        temp_ls.append(curr_node.val)
        curr_node = curr_node.next
    carry = 1
    for idx in range(1, len(temp_ls) + 1):
        if temp_ls[-idx] + carry == 10:
            temp_ls[-idx] = 0
            carry = 1
        else:
            carry = 0
            temp_ls[-idx] += 1
            break

    if carry == 1:
        temp_ls.insert(0, 1)

    head = curr = ListNode(0)
    for num in temp_ls:
        n = ListNode(num)
        curr.next = n
        curr = n

    return head.next


def plusOne_approach2(head: ListNode) -> ListNode:
    """
    Algorithm:
    1. find last non 9 node.
    2. Add one to the above node
    3. zero all the nine nodes after last non nine node
    4. To handle 9 -> 9 ->9 use dummy node logic
    :param head:
    :return:
    """
    dummy_node = ListNode(0)
    dummy_node.next = head
    non_nine = dummy_node
    while head:
        if head.val != 9:
            non_nine = head
        head = head.next
    non_nine.val += 1
    non_nine = non_nine.next
    while non_nine:
        non_nine.val = 0
        non_nine = non_nine.next

    return dummy_node if dummy_node.val else dummy_node.next



