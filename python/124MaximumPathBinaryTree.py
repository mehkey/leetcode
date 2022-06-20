# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        
        """
        
        maximum path = 0
        
        minimum path = 0
        
        try again = 0
        
        
        """
        
        self.maximum = root.val
        
        #print(maximum)
        
        def dfs(node):
            
            if not node:
                return 0
            
            maxleft = max(dfs(node.left),0)
            maxright = max(dfs(node.right),0)
            
            self.maximum = max(self.maximum, maxleft + maxright + node.val  )
            
            return node.val + max( maxleft, maxright)

            
        dfs(root) 
        
        return self.maximum