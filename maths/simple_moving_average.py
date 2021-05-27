from queue import Queue


class SMA:
    def __init__(self, window):
        self.window = window
        self.price_queue = Queue()
        self.sum = 0

    def sma(self, price):
        if self.price_queue.qsize() < self.window:
            self.sum += price
            self.price_queue.put(price)
            return self.sum / self.price_queue.qsize()

        self.sum -= self.price_queue.get()
        self.sum += price
        self.price_queue.put(price)
        return self.sum / self.window

if __name__ == '__main__':
    sma = SMA(3)
    print(sma.sma(1))
    print(sma.sma(2))
    print(sma.sma(3))
    print(sma.sma(4))
    print(sma.sma(5))

