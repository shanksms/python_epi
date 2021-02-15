class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return NotImplemented
        return self.data == other.data and self.next == other.next

