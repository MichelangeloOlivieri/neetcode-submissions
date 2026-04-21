# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        """
        1) No empty input; example on paper
        2) Dfs solution
        """

        res = 0

        def dfs(node, max_val):

            nonlocal res

            if node.val >= max_val:
                res += 1

            if node.left:
                dfs(node.left, max(node.val, max_val))
            if node.right:
                dfs(node.right, max(node.val, max_val))

        dfs(root, -float('inf'))
            
        return res     

        """
        3) Ok
        4) Time complexity O(n), where n is the number of nodes; space complexity 
        O(n)
        """  