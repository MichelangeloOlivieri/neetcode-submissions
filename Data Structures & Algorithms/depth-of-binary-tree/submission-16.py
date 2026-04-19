# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # recursive bfs solution

        if not root:
            return 0

        level = 0
        q = deque([root])

        def bfs(q):
            nonlocal level

            if not q:
                return
                
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
            bfs(q)

        bfs(q)
        return level

        """
        Time complexity O(n), where n is the number of nodes; space complexity 
        O(2^[log(n) - 1]) = O(n), which is the maximum length of the queue
        """