# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        """
        1) Usual edge cases and stuff
        2) Recursive implementation
        """

        if not root:
            return 0

        depth = 1
        depth = max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1, depth)

        return depth

        """
        3) Dry run: seems ok
        4) Time complexity O(n); space complexity O(n)
        """


        