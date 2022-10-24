
class Node:
    def __init__(self, val, neighbours=None):
        self.val = val
        if neighbours is None:
            neighbours = []
        self.neighbours = neighbours
