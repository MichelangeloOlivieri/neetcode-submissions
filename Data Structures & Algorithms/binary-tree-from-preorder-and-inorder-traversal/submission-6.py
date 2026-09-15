# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder or len(preorder) != len(inorder):
            return None

        inorder_index = {}
        for i in range(len(inorder)):
            inorder_index[inorder[i]] = i

        root_index = 0

        def dfs(l, r):
            nonlocal root_index

            if l > r:
                return None

            root_val = preorder[root_index]
            root_index += 1
            root = TreeNode(root_val)
            mid = inorder_index[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        return dfs(0, len(inorder) - 1)

        """
        - Time complexity O(n), where n = len(preorder) = len(inorder)
        - Space complexity O(n)
        """