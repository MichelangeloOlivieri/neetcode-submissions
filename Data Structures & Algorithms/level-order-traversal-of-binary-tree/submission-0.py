# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        """
        1) Edge cases like empty root
        2) Bfs method
        """

        if not root:
            return []

        stack = [[root, 1]]
        res = [[]]

        while stack:
            node, depth = stack.pop()

            if len(res) < depth:
                res.append([])
            res[depth - 1].append(node.val)

            if node.right:
                stack.append([node.right, depth + 1])
            if node.left:
                stack.append([node.left, depth + 1])

        return res

        """
        3) Dry run: seems ok
        4) Time complexity O(n) where n is the number of nodes; space complexity O(n)
        """

        