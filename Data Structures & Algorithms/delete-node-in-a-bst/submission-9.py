# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return None

            if node.val > key:
                node.left = dfs(node.left)
            elif node.val < key:
                node.right = dfs(node.right)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                curr = node.right
                while curr.left:
                    curr = curr.left

                node.val = curr.val
                node.right = self.deleteNode(node.right, curr.val)
                
            return node

        return dfs(root)

        """
        - Time complexity O(h), where h is the height of the tree (typically h = log(n))
        - Space complexity O(h)
        """