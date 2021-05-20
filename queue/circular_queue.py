class Queue:
    SCALE_FACTOR = 2
    def __init__(self, initial_size):
        self.arr = [None] * initial_size
        self.head = 0
        self.tail = 0
        self.current_size = 0

    def enqueue(self, element):
        if self.current_size == len(self.arr):
            print('Queue is full. Current size ', len(self.arr))
            self.arr = (self.arr[self.head:] + self.arr[:self.head])
            self.head, self.tail = 0, self.current_size
            self.arr += [None] * (
                    len(self.arr) * Queue.SCALE_FACTOR - len(self.arr)
            )
        self.arr[self.tail] = element
        self.tail = (1 + self.tail) % len(self.arr)
        self.current_size += 1

    def dequeue(self):
        element = None
        if self.current_size == 0:
            raise ValueError('size of the queue is 0')
        else:
            element = self.arr[self.head]
            self.head = (1 + self.head) % len(self.arr)
            self.current_size -= 1
        return element

if __name__ == '__main__':
    queue = Queue(2)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())


