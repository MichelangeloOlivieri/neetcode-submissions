class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        """
        1) Assuming only valid numbers (root.val != 0)
        2) Use a dfs and when you reach a leaf node you sum the number
        """

        if not root:
            return 0

        res = 0

        def dfs(node, partial):
            nonlocal res
            partial = partial * 10 + node.val

            if not node.left and not node.right:
                res += partial
            else:
                if node.left:
                    dfs(node.left, partial)
                if node.right:
                    dfs(node.right, partial)

        dfs(root, 0)
        return res

        """
        3) Ok
        4) Time complexity O(n), where n is the number of nodes; space complexity O(n)
        """