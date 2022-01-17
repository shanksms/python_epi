"""
Problem: You are given a list of Stars. assume earth is at 0, 0, 0. You need to return k closest stars to earth
Algorithm:
stars --> []
max_heap = []
k --> int
1. for star in stars:
    if len(max_heap) == k:
        heapq.pushpop(max_heap, star)
    heapq.push(star)
2. return max_heap
"""
import math
from typing import List
import heapq


class Star:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    '''
    def __lt__(self, other):
        return self.distance - other.distance
    '''
    def __eq__(self, other):
        return self.distance == other.distance

    def __str__(self):
        return '({x}, {y}, {z})'.format(x=self.x, y=self.y, z=self.z)

    def __repr__(self):
        return 'Star({x}, {y}, {z})'.format(x=self.x, y=self.y, z=self.z)


def closest_star(stars: List, k: int):
    max_heap = []
    for star in stars:
        if len(max_heap) == k:
            heapq.heappushpop(max_heap, (-star.distance, star))
        else:
            heapq.heappush(max_heap, (-star.distance, star))
    return [s[1] for s in max_heap]


if __name__ == '__main__':
    s1 = Star(1, 1, 1)
    s2 = Star(2, 2, 2)
    s3 = Star(3, 3, 3)
    print(closest_star([s1, s2, s3], 2))



