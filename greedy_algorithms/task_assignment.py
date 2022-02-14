from collections import namedtuple
from typing import List

"""
Algorithm:
result = []
input_durations = [6, 4, 5, 4, 1, 2]
1. Sort input_durations
2. for i in range(len(input_durations) // 2):
        task1, task2 =  input_durations[i], input_durations[-i]
        result.append([task1, task2])
3. return result
"""
task_pair = namedtuple('task_pair', ['task_1', 'task_2'])


def optimal_task_assignment(durations: List[int]):
    durations = sorted(durations)
    result = []
    for counter in range(len(durations) // 2):
        result.append(task_pair(durations[counter], durations[-(counter + 1)]))
    return result


if __name__ == '__main__':
    print(optimal_task_assignment([6, 4, 5, 4, 1, 2]))