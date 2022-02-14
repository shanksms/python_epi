
"""
Given service times of a set of queries, find the optimal sequencing so that waiting time is minimum.
Database can execute one query at a time
Algo:
input = [2, 5, 1, 3]
result = []
running_sum = 0
1. sort the input in ascending order
    input = sorted(input)
2. for service_time in input:
        running_sum +=  service_time
        result.append(running_sum)
3. return result[:len(input) - 1]
"""
from typing import List


def solution(service_times: List[int]):
    service_times = sorted(service_times)
    result = []
    running_sum = 0
    for service_time in service_times:
        running_sum += service_time
        result.append(running_sum)
    return result[:len(service_times) - 1]


if __name__ == '__main__':
    print(solution([2, 5, 1, 3]))