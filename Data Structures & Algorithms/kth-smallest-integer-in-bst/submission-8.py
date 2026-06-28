class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        """
        1) Ok
        2) Stack data structure
        """

        stack = []
        curr = root
        n = 0

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
            

            

            
