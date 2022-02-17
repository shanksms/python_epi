"""
Consider a Foreman responsible for a number of tasks on the factory floor. Each task starts at a fixed time and ends
at a fixed time. The foreman wants to visit the floor to check on the tasks. Your job is to help him minimize the number of
visits he makes. In each visit he can check the tasks taking place at that time.

For example, if there are tasks at times [0, 3], [2, 6], [3, 4], [6, 9]
visit times could be 3, 6. 0, 2, 3, 6 is also ans answer but it is not an optimal answer.
Algorithm:
input = [Interval(0, 3), Interval(2, 6), Interval(3, 4), Interval(6, 9)]
visit_list = []
1. Sort the input by end time in ascending order
    input = sorted(input, key=interval.right)
2. Loop over the list. If last visit time is less than the left of the current interval, add right of the current interval to
    the possible visit list.
    last_visit_time = float(-inf)
    for interval in input:
        if interval.left > last_visit_time:
            visit_list.append(interval.right)
            last_visit_time = interval.right



"""
import collections
from math import inf
from typing import List

Interval = collections.namedtuple('Interval', ['left', 'right'])


def find_number_of_visits(intervals: List[Interval]):
    intervals = sorted(intervals, key=lambda interval: interval.right)
    possible_visit_times = []
    last_visit_time = float(-inf)
    for interval in intervals:
        if interval.left > last_visit_time:
            possible_visit_times.append(interval.right)
            last_visit_time = interval.right

    return possible_visit_times



if __name__ == '__main__':
    intervals = [Interval(0, 3), Interval(2, 6), Interval(3, 4), Interval(6, 9)]
    print(find_number_of_visits(intervals))

