# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        """
        1) Usual edge cases
        2) Visit all nodes, create a list from them, order it, and return the requested value
        """

        if not root:
            return None

        nodes = self.visitBinaryTree(root) # already sorted because it is a BST!

        if k > len(self.visitBinaryTree(root)):
            return None
        else:
            return self.visitBinaryTree(root)[k - 1]

    def visitBinaryTree(self, root):

        if not root:
            return []

        left = self.visitBinaryTree(root.left)
        right = self.visitBinaryTree(root.right)

        return left + [root.val] + right


        """
        3) Syntax and dry run: seems ok
        4) Time complexity O(n) where n is the number of nodes; space complexity O(n)
        """
