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

        # 1. Search Phase: Traverse to find the node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # 2. Deletion Phase: Node found (key == root.val)
            
            # Case A: No left child (covers both 0 children and 1 right child)
            if not root.left:
                return root.right
            
            # Case B: No right child (covers 1 left child)
            elif not root.right:
                return root.left
            
            # Case C: 2 children
            # Find the In-Order Successor (Minimum value in the right subtree)
            curr = root.right
            while curr.left:
                curr = curr.left
            
            # Overwrite current node's value with the successor's value
            root.val = curr.val
            
            # Recursively delete the successor node from the right subtree
            root.right = self.deleteNode(root.right, root.val)

        # Return the cleanly stitched root up the call stack
        return root

        # ==========================================
        # Time Complexity: O(H), where H is the height of the tree. 
        #                  Average case O(log N), Worst case O(N) for skewed trees.
        # Space Complexity: O(H) for the call stack during recursion.
        # ==========================================