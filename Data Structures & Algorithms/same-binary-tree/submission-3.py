# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # recursive dfs solution

        def dfs(first, second):
            if not first and not second:
                return True
            if not first or not second or first.val != second.val:
                return False

            return dfs(first.left, second.left) and dfs(first.right, second.right)
        
        return dfs(p, q)

        """
        Time complexity O(n), where n is the number of nodes; space complexity O(n)
        """