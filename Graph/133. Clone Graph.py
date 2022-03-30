"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        - hasmap: old, new columns
        - create copy of the first node
        - map original node to the new node
        - 
        """
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                #already made the clone
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))
                #return the copy we made
            return copy
        
        return dfs(node) if node else None
