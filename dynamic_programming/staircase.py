

"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


def climb_stairs(steps: int) -> int:
    if steps == 1 or steps == 2:
        return steps
    result = [0] * (steps + 1)
    result[1] = 1
    result[2] = 2
    for n in range(3, len(result)):
        result[n] = result[n-1] + result[n-2]
    return result[steps]


if __name__ == '__main__':
    print(climb_stairs(3))
