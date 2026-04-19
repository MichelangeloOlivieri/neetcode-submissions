# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # iterative bfs solution

        if not root:
            return 0

        level = 0
        q = deque([root])

        while q: 
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            level += 1
        
        return level

        """
        Time complexity O(n), where n is the number of nodes; space complexity 
        O(2^[log(n) - 1]) = O(n), which is the maximum length of the queue
        """