# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        
        if not root and not subroot:
            return True
        
        if not root or not subroot:
            return False
        
        def isSub(r, s):
            
            if not r and not s:
                return True
            
            if not r or not s:
                return False
            
            if r.val != s.val:
                return False
            
            return isSub(r.left,s.left) and isSub(r.right,s.right)
        
        if isSub(root,subroot):
            return True
        
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right,subroot)
        
        
        
        
            
            