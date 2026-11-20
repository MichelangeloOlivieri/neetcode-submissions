"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        clone = {node : Node(node.val, [])}

        def dfs(node):
            for nei in node.neighbors:
                if nei not in clone:
                    clone[nei] = Node(nei.val, [])
                    dfs(nei)
                clone[node].neighbors.append(clone[nei])

        dfs(node)
        return clone[node]
    
"""
- Time complexity: O(E + V), where E = #{edges} and V = #{vertices}.
- Space complexity: O(V).
"""