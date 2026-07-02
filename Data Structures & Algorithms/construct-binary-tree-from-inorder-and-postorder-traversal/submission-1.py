class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:

        """
        1) Assuming the input is valid (inorder and postorder have the same length, 
        and the same values - meaning one is a particular and valid permutation of
        the other)
        2) Recursion
        """

        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[: index], postorder[: index])
        root.right = self.buildTree(inorder[index + 1 :], postorder[index : -1])

        return root

        """
        3) Ok
        4) Time complexity O(n^2), where n = len(inorder); space complexity O(n^2)
        """
