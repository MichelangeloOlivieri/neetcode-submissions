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

        """
        1) Divide the grid into four subgrids recursively and assign the values to the
        nodes (subgrids)
        2) Recursive solution on subgrids; you divide into subgrids every time you
        find two different values in the grid
        """

        if not grid:
            return None
        
        if len(grid) == 1:
            return Node(grid[0][0] == 1, True, None, None, None, None)

        n = len(grid)
        mid = n // 2
        split = False
        top_left = [[] for _ in range(mid)]
        top_right = [[] for _ in range(mid)]
        bottom_left = [[] for _ in range(mid)]
        bottom_right = [[] for _ in range(mid)]

        for i in range(n):
            for j in range(n):

                if i < mid and j < mid:
                    top_left[i].append(grid[i][j])
                elif i < mid and j >= mid:
                    top_right[i].append(grid[i][j])
                elif i >= mid and j < mid:
                    bottom_left[i - mid].append(grid[i][j])
                elif i >= mid and j >= mid:
                    bottom_right[i - mid].append(grid[i][j])

                if grid[i][j] != grid[0][0]:
                    split = True

        if split:
            topLeft = self.construct(top_left)
            topRight = self.construct(top_right)
            bottomLeft = self.construct(bottom_left)
            bottomRight = self.construct(bottom_right)
            root = Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
        else:
            root = Node(grid[0][0] == 1, True, None, None, None, None)

        return root

        """
        Time complexity O(n^2); space complexity O(n^2)
        """


        
        