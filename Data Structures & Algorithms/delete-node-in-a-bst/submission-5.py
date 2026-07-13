class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # ==========================================
        # Clarifying Questions (Implicit):
        # - Are node values unique? (Yes, standard BST property).
        # - What if the key doesn't exist? (Return the original tree unaltered).
        #
        # Algorithm Description:
        # Recursively search for the node. If found, handle the 3 standard BST deletion cases (0, 1, or 2 children), using the In-Order Successor to cleanly resolve the 2-children case without violating the BST invariant.
        # ==========================================

        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            curr = root.right
            while curr.left:
                curr = curr.left
            
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)
            
        return root

        # ==========================================
        # Time Complexity: O(H), where H is the height of the tree. 
        #                  Average case O(log N), Worst case O(N) for skewed trees.
        # Space Complexity: O(H) for the call stack during recursion.
        # ==========================================