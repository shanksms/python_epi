import pytest
from linkedlist_algorithms.cycle_in_linkedlist import check_cycle
from linkedlist_algorithms.linkedlist import ListNode


def build_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head


def test_empty_list():
    assert check_cycle(None) is False

def test_single_node_no_cycle():
    head = ListNode(1)
    assert check_cycle(head) is False


def test_single_node_with_self_cycle():
    head = ListNode(1)
    head.next = head
    assert check_cycle(head) is True

def test_two_nodes_no_cycle():
    head = build_linked_list([1, 2])
    assert check_cycle(head) is False


def test_two_nodes_with_cycle():
    head = build_linked_list([1, 2])
    head.next.next = head
    assert check_cycle(head) is True