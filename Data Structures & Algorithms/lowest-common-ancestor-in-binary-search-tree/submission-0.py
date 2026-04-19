# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        """
        1) One edge case is where p = q, or the tree is empty, or p and/or q are None; I am 
        assuming that p and q actually belong to the tree
        2) Maybe a recursive approach, visiting each node, would do
        """

        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
            
        """
        3) Dry run: seems ok
        4) Time complexity O(log(n)) (because log(n) is the height of the tree); space 
        complexity O(1)
        """


