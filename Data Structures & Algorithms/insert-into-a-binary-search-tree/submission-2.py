# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        """
        1) Example seen
        2) Tree, PreOrder Traversal
        """

        def dfs(node):
            if not node:
                return TreeNode(val)

            if val < node.val:
                node.left = dfs(node.left)
            elif val > node.val:
                node.right = dfs(node.right)

            return node

        return dfs(root)

        """
        Time complexity O(n), where n is the number of nodes; space complexity O(n)
        """