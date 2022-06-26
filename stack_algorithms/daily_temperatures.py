"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i]
is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for
which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    answers = [0] * n
    stack = []
    for curr_day, curr_temp in enumerate(temperatures):
        if stack and temperatures[stack[-1]] < curr_temp:
            prev_day = stack.pop()
            answers[prev_day] = curr_day - prev_day
        stack.append(curr_day)
    return answers



if __name__ == '__main__':
    print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
