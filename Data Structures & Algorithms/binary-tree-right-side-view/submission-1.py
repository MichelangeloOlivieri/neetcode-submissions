# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        """
        1) Empty input; example on paper
        2) Maybe a bfs approach
        """

        if not root:
            return []

        res = []
        q = collections.deque()
        q.append(root)

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(node.val)

        return res

        """
        3) Ok
        4) Time complexity O(n), where n is the number of nodes; space complexity
        O(n)
        """