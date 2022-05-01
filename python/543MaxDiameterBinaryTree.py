# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        maxDiameter = [0] *1

        
        def dfs(node):
            #print(node.val)
            if not node:
                return 0
            
            leftHeight = dfs(node.left) 
            rightHeight = dfs(node.right)
            
            height = max(leftHeight, rightHeight) + 1
            
            maxDiameter[0] = max(maxDiameter[0], leftHeight + rightHeight)

            return height

        dfs(root)
        
        return maxDiameter[0]