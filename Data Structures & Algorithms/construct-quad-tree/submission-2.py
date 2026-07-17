"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        if not grid:
            return None

        def dfs(r, c, n):
            if n == 1:
                return Node(grid[r][c] == 1, True, None, None, None, None)

            half = n // 2
            topLeft = dfs(r, c, half)
            topRight = dfs(r, c + half, half)
            bottomLeft = dfs(r + half, c, half)
            bottomRight = dfs(r + half, c + half, half)

            all_leaves = (topLeft.isLeaf and 
                topRight.isLeaf and 
                bottomLeft.isLeaf and 
                bottomRight.isLeaf)
            all_same_value = (topLeft.val == 
                topRight.val == 
                bottomLeft.val == 
                bottomRight.val)

            if all_leaves and all_same_value:
                return Node(topLeft.val, True, None, None, None, None)
                
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(0, 0, len(grid))    

        """
        Time complexity O(n^2); space complexity O(log(n))
        """ 
        