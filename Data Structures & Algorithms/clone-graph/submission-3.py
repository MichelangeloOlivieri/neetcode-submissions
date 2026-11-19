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

        q = deque([node])
        clone = {node : Node(node.val, [])}

        while q:
            curr = q.popleft()
            for nei in curr.neighbors:
                if nei not in clone:
                    clone[nei] = Node(nei.val, [])
                    q.append(nei)
                clone[curr].neighbors.append(clone[nei])

        return clone[node]

"""
- Time complexity: O(E + V), where E = #{edges} and V = #{vertices}.
- Space complexity: O(V).
"""