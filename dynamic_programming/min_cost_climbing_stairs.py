"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.



Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
https://leetcode.com/problems/min-cost-climbing-stairs/
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        1. find min cost for reaching index n-1 and n- 22
        2. To reach next index with min cost, find out cost to go from n-2 and n-1.
        3. min of above two, will be stored in the result
        """
        result = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            cost_for_one_step = result[i - 1] + cost[i - 1]
            cost_for_two_step = result[i - 2] + cost[i - 2]
            result[i] = min(cost_for_one_step, cost_for_two_step)
        return result[-1]
