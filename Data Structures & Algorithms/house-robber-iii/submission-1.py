# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        memo = {}
        
        def dfs(node, can_rob):
            if not node:
                return 0
            if (node, can_rob) in memo:
                return memo[(node, can_rob)]

            leave = dfs(node.left, True) + dfs(node.right, True)

            if can_rob:
                take = node.val + dfs(node.left, False) + dfs(node.right, False)
            else:
                take = leave

            memo[(node, can_rob)] = max(leave, take)
            return memo[(node, can_rob)]

        return dfs(root, True)
