# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        """
        1) [1, 2, 3, 4, 5, 6, 7] -> [1, 2, 4, 5, 3, 6, 7]
        2) Preorder Traversal
        """

        res = [] 

        def dfs(node):
            if not node:
                return

            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
            return

        dfs(root)
        return res  

        """
        - Time complexity O(n), where n = #{nodes}
        - Space complexity O(n)
        """   