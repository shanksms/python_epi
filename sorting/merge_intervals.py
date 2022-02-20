"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Algorithm
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    result = [[1,3]]
    sort the arrays in intervals by first element.
    for idx in range(1, len(intervals)):
        if intervals[idx][0] >= result[-1][1]:
            # We need to merge
            merged_interval = [result[-1][0], intervals[idx][1]]
            result[-1] = merged_interval
        else:
            result.append(intervals[idx])
    :param intervals:
    :return:
    """
    intervals = sorted(intervals, key=lambda interval: interval[0])
    result = [intervals[0]]
    for idx in range(1, len(intervals)):
        if intervals[idx][0] <= result[-1][1]:
            # We need to merge
            if intervals[idx][1] > result[-1][1]:
                merged_interval = [result[-1][0], intervals[idx][1]]
                result[-1] = merged_interval
        else:
            result.append(intervals[idx])
    return result


if __name__ == '__main__':
    print(merge_intervals([[1, 4], [4, 5]]))
    print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
