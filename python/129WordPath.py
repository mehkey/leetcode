# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        """
        
        KEEP A GLOBAL COUNTER SUM
        
        DFS BFS 
        
        (DFS)
        
        FIND A LEAF (NO RIGHT AND LEFT CHILD) -> ADD TO COUNTER
        
        """
        
        self.sum = 0
        
        def dfs(node, pathsum):
            
            if not node: #None
                return
            
            if not node.left  and not node.right:
                self.sum += int(str(pathsum) + str(node.val))
            
            
            dfs(node.left, int(str(pathsum) + str(node.val)) )
            
            dfs(node.right, int(str(pathsum) + str(node.val)))

        
        dfs(root, 0)
        
        return self.sum
        
