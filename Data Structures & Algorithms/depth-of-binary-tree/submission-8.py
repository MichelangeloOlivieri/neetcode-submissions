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

        stack = [[root, 1]]
        max_depth = 1
        
        while stack:
            node, depth = stack.pop() 
            if node.left:
                new_node = node.left
                stack.append([new_node, depth + 1])
                max_depth = max(max_depth, depth + 1)
            if node.right:
                new_node = node.right
                stack.append([new_node, depth + 1])
                max_depth = max(max_depth, depth + 1)

        return max_depth