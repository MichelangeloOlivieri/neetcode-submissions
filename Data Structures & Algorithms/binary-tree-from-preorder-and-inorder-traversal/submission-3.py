# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
            
        inorder_index_map: Dict[int, int] = {val: idx for idx, val in enumerate(inorder)}
        preorder_idx: int = 0
        
        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_idx
            
            # Base case: if the logical window collapses, there are no elements to construct.
            if left > right:
                return None
            
            # The current root value is strictly determined by the preorder array.
            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)
            preorder_idx += 1
            
            # Find the split point in the inorder array.
            mid = inorder_index_map[root_val]
            
            # Recursively build the left and right subtrees utilizing the split bounds.
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
            
        return build(0, len(inorder) - 1)