# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # iterative dfs solution
        
        first = [p]
        second = [q]
        while first and second:
            node1 = first.pop()
            node2 = second.pop()
            if node1 or node2:
                if not node1 and node2 or node1 and not node2 or node1.val != node2.val:
                    return False
                first.append(node1.left)
                second.append(node2.left)
                first.append(node1.right)
                second.append(node2.right)

        return True

        """
        Time complexity O(n), where n is the total number of nodes of the two trees;
        space complexity O(n)
        """