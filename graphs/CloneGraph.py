"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#Given a reference of a node in a connected undirected graph.
#Return a deep copy (clone) of the graph.


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        exists={}
        
        def clone(node):
            if node in exists: 
                return exists[node]
            
            copy = Node(node.val)             #copy that nodes value
            exists[node] = copy               #put that value in our existing nodes set
            for n in node.neighbors:           #iterate through our nodes neighbors
                copy.neighbors.append(clone(n)) #returns copy we create clones neighbors recursively
            return copy
        return clone(node) if node else None      #return graph
