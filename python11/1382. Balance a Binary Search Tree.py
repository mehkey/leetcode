# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        trav = []
        
        def dfs(node):
            if not node:
                return
            trav.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        trav.sort()
        
        def dfs( cur):
            if not cur:
                return None

            mid = len(cur) // 2
            
            nn = TreeNode(cur[mid])
            
            nn.left = dfs( cur[0:mid])
            
            nn.right = dfs( cur[mid+1:])
            
            return nn

        return dfs(trav)

