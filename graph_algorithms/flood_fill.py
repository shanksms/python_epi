"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the
starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color),
and so on. Replace the color of all of the aforementioned pixels with color.
https://leetcode.com/problems/flood-fill/
"""
from typing import List


class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == color:
            return image
        R, C = len(image), len(image[0])

        def dfs(r, c):
            if start_color == image[r][c]:
                image[r][c] = color
                if r >= 1:
                    dfs(r - 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if r < R - 1:
                    dfs(r + 1, c)
                if c < C - 1:
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image

