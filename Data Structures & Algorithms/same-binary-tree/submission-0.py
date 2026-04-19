# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        """
        1) Usual edge cases
        2) Recursive implementation
        """

        if not p and not q:
            return True
        if p and not q or not p and q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        """
        3) Dry run: seems ok
        4) Time complexity O(n); space complexity O(n)
        """
        