# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def visitNode(node, maxLeft, maxRight):
            
            if not node:
                return True
            
            if node.val <= maxLeft:
                return False

            if node.val >= maxRight:
                return False

            return visitNode(node.left,maxLeft, node.val) and visitNode(node.right, node.val, maxRight)

        return visitNode(root, float("-inf"), float("inf"))

