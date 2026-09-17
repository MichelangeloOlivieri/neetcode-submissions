# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        res = []
        q = deque()
        q.append(root)
        count = 1

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if count:
                    res.append(node.val)
                    count -= 1
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            count = 1

        return res

        """
        T: O(n), S: O(n)
        """   