from typing import List
import heapq

"""
in this problem, each element is at most k position away from 
its actual position
Algorithm:
a -> input_array
r -> result
heap --> min_heap
1. create a min heap
2. put k+1 elements from the A to heap
3. loop a from k+1 to len(a)
    a. result.append(heap.pushpop(heap, a[i]))
4. loop the heap until it is empty:
    result.append(heap.pop())

"""


def sort_almost_sorted_array(input_list: List, k: int):
    result = []
    min_heap = []
    for i in range(k+1):
        heapq.heappush(min_heap, input_list[i])
    for i in range(k+1, len(input_list)):
        result.append(heapq.heappushpop(min_heap, input_list[i]))
    while min_heap:
        result.append(heapq.heappop(min_heap))
    return result

if __name__ == '__main__':
    print(sort_almost_sorted_array([3, 2, 1, 4, 5], 2))
