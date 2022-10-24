"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
"""
from graph_algorithms.node import Node


class Solution(object):

    def __init__(self):
        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        self.visited = {}

    def clone_graph(self, node: Node) -> Node:
        '''
        Algorithm: Following algorithm uses DFS
        :param node:
        :return:
        '''

        if node is None:
            return None
        # If we already visited the node, return it. otherwise it will be an infinite loop.
        if node in self.visited:
            return self.visited[node]
        # Clone the node. Since we don't know the neighbours, we pass an empty list
        cloned_node = Node(node.val, [])
        self.visited[node] = cloned_node

        if node.neighbours:
            cloned_node.neighbours = [self.clone_graph(n) for n in node.neighbours]
        return cloned_node
