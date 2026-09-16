# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_val):
            if not node:
                return 0
            
            count = 0
            if node.val >= max_val:
                count += 1

            count_left = 0
            count_right = 0
            if node.left:
                count_left = dfs(node.left, max(node.val, max_val))
            if node.right:
                count_right = dfs(node.right, max(node.val, max_val))

            return count + count_left + count_right
 
        return dfs(root, -float('inf'))     

        """
        - Time complexity O(n), where n = #{nodes}
        - Space complexity O(n)
        """  