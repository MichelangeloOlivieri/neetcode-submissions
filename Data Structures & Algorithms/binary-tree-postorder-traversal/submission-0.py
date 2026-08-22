# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        """
        1) Example seen
        2) Tree, PostOrder Traversal
        """

        res = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            dfs(node.right)

            res.append(node.val)
            return

        dfs(root)
        return res

        """
        3) dfs(1) -> dfs(2) -> dfs(4) -> res = [4]
                            -> dfs(5) -> res = [4, 5]
                            -> res = [4, 5, 2]

                  -> dfs(3) -> dfs(6) -> res = [4, 5, 2, 6]
                            -> dfs(7) -> res = [4, 5, 2, 6, 7]
                            -> res = [4, 5, 2, 6, 7, 3]
          -> res = [4, 5, 2, 6, 7, 3, 1]
        4) Time complexity O(n), where n is the number of nodes; space complexity O(n)
        """
        