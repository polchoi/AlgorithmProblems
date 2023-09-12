# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = root
        sec_root = root
        while root.val != p.val and sec_root.val != q.val:
            if root.val < p.val:
                root = root.right
            elif root.val > p.val:
                root = root.left
            
            if sec_root.val < q.val:
                sec_root = sec_root.right
            elif sec_root.val > q.val:
                sec_root = sec_root.left
            
            if root.val == sec_root.val:
                lca = root
            else:
                break
        return lca