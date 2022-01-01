from queue import PriorityQueue
from typing import List

def solve(num_arr : List[int]):
    pq = PriorityQueue()
    num1 = []
    num2 = []
    for num in num_arr:
        pq.put(num)
    while not pq.empty():
        num1.append(str(pq.get()))
        if not pq.empty():
            num2.append((str(pq.get())))
    print(num1)
    print(num2)
    return int(''.join(num1)) + int(''.join(num2))


if __name__ == '__main__':
    print(solve([ 6, 8, 4, 5, 2, 3 ]))
