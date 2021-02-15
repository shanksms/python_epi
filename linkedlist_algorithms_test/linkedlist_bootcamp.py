import unittest
from linkedlist_algorithms.linkedlist import ListNode
from linkedlist_algorithms import linkedlist_bootcamp

class MyTestCase(unittest.TestCase):
    def test_search_node(self):
        child = ListNode(2, None)
        root = ListNode(1, child)
        expected = ListNode(2, None)
        self.assertEqual(linkedlist_bootcamp.search_node(root, child), expected)


if __name__ == '__main__':
    unittest.main()
