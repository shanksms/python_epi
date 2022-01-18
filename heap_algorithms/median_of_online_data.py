import heapq

"""
Algorithm:
min_heap = []
max_heap = []
input --> e
1.  heap.push(max_heap, -heap.pushpop(min_heap, e))
2. if len(max_heap) > len(min_heap):
        heap.push(min_heap, -heap.pop(max_heap))
3. return 0.5 * (heap.peek(min_heap) + (-heap.peek(max_heap))) if len(max_heap) ==  len(min_heap) else heap.peek(min_heap)

"""

class Median:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def median(self, number: float) -> float:
        heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, number))
        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        return 0.5 * (self.min_heap[0] - self.max_heap[0]) if len(self.max_heap) == len(self.min_heap) else self.min_heap[0]

if __name__ == '__main__':
    median = Median()
    print(median.median(1))
    print(median.median(2))
    print(median.median(3))


