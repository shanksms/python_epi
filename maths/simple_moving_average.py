from queue import Queue
from collections import deque

class SMA:
    def __init__(self, window):
        self.window = window
        self.queue = deque()
        self.moving_sum = 0
    def sma(self, price):
        self.queue.append(price)
        if len(self.queue) <= self.window:
            self.moving_sum += price
        else:
            popped_price = self.queue.popleft()
            self.moving_sum -= popped_price
            self.moving_sum += price
        return self.moving_sum / len(self.queue)


if __name__ == '__main__':
    sma = SMA(3)
    assert sma.sma(1) == 1.0
    assert sma.sma(2) == 1.5
    assert sma.sma(3) == 2.0
    assert sma.sma(4) == 3.0
    assert sma.sma(5) == 4.0

