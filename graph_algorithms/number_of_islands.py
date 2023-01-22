
"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
https://leetcode.com/problems/number-of-islands/
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if grid[r][c] != '1':
                return
            grid[r][c] = 'V'
            if r >= 1:
                dfs(r - 1, c)
            if c >= 1:
                dfs(r, c - 1)
            if r < R - 1:
                dfs(r + 1, c)
            if c < C - 1:
                dfs(r, c + 1)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
        return count