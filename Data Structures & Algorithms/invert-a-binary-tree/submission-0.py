# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        """
        1) Edge cases like empty tree and stuff
        2) Recursive implementation
        """

        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left)
        self.invertTree(root.right) 

        return root

        """
        3) Dry run: seems ok
        4) Time complexity O(n); space complexity O(1)
        """
