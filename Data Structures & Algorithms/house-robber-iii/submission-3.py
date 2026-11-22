# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return [0, 0]

            left = dfs(node.left)
            right = dfs(node.right)
            take = node.val + left[1] + right[1]
            leave = max(left) + max(right) 

            return [take, leave]

        return max(dfs(root))

"""
- Time complexity: O(n), where n = #{nodes}.
- Space complexity: O(n) for the recursion stack.
"""