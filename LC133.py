"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        old_to_clone = {node: Node(node.val)}
        stack = [node]
        while stack:
            curr = stack.pop()
            for i in curr.neighbors:
                if i not in old_to_clone:
                    old_to_clone[i] = Node(i.val)
                    stack.append(i)
                old_to_clone[curr].neighbors.append(old_to_clone[i])
        return old_to_clone[node]
