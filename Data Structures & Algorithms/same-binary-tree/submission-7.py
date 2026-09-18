# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(first, second):
            if not first:
                return not second
            if not second:
                return not first

            is_same_value = (first.val == second.val)
            is_same_left = dfs(first.left, second.left)
            is_same_right = dfs(first.right, second.right)
            
            return is_same_value and is_same_left and is_same_right

        return dfs(p, q)        