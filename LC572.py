# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root, subRoot):
            if root is None and subRoot is None:
                return True
            if (root is None and subRoot is not None) or (root is not None and subRoot is None):
                return False
            return root.val == subRoot.val and isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)
        
        if root:
            if not isSameTree(root, subRoot):
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            else:
                return True
        else:
            return False               
