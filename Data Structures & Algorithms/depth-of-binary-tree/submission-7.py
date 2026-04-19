# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        count = {root : 1}
        max_depth = 1

        def dfs(node, depth):
            nonlocal max_depth 
            
            if node.left:
                new_node = node.left
                count[new_node] = depth + 1
                max_depth = max(max_depth, depth + 1)
                dfs(new_node, depth + 1)
            if node.right: 
                new_node = node.right
                count[new_node] = depth + 1
                max_depth = max(max_depth, depth + 1)
                dfs(new_node, depth + 1)

        dfs(root, 1)
        return max_depth

        # tempo O(n) dove n numero nodi, spazio O(log(n))

        

        