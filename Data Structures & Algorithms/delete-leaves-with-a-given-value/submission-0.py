# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        """
        1) Example seen
        2) Tree, Preorder dfs
        """
        if not root:
            return None

        dummy = TreeNode(0, root, None)

        def dfs(node):
            if not node:
                return None
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            if not node.left and not node.right and node.val == target:
                return None
            else:
                return node

        dummy = dfs(dummy)
        return dummy.left

        """
        Time complexity O(n) where n is the number of nodes; space complexity O(n)
        """

