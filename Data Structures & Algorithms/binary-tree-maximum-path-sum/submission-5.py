# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        """
        1) Empty input; are negative integers allowed?
        2) - Solution 1: dfs calculating each possible path; use a similar approach to
        Kadane's algorithm, ie visit the tree "starting" from the leaves and come back
        keeping just the brenches which contribute positively
        """

        if not root:
            return 0
        
        max_sum = -float('inf')

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0

            # Stile Kadane: se un ramo è negativo, non lo prendiamo (mettiamo 0)
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Valutiamo l'arco chiuso che passa per questo nodo
            max_sum = max(max_sum, node.val + left + right)

            # Ritorniamo al genitore solo UN ramo (il migliore), perché un path non può biforcarsi due volte
            return node.val + max(left, right)

        dfs(root)
        return max_sum

        """
        3) Ok
        4) Time complexity O(n), where n is the number of nodes; space complexity O(1)
        """