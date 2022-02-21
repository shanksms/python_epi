from collections import deque


class MinStack:
    """
    Algorithm
    1. Create two dequeues: one as a stack and other to keep track of min elements seen so far.
    2. while pushing,
        a. if new element is less than the minimum element in min stack, pus this new element to min stack
        b. if not, dont push new element to new stack
    3. while popping, check if you are popping out the min value, if yes then pop out from the min stack as well


    """

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.appendleft(val)
            if val <= self.min_stack[0]:
                self.min_stack.appendleft(val)
        else:
            self.stack.appendleft(val)
            self.min_stack.appendleft(val)

    def pop(self) -> None:
        if self.stack[0] == self.min_stack[0]:
            self.min_stack.popleft()
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.min_stack[0]


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()
    minStack.pop()
    minStack.top()
    minStack.getMin()
