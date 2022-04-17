# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node) -> List[int]:
            
            rightValues = [0,0]
            leftValues = [0,0]
            
            if node.left :
                leftValues = dfs(node.left)
            
            if node.right :
                rightValues = dfs(node.right)
            
            currentValue = [node.val + leftValues[1] + rightValues[1], leftValues[0] + rightValues[0]]
            
            return currentValue
        
        rootValue = dfs(root)
        
        return max(rootValue[0],rootValue[1])
        

        