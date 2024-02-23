# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res = []
        @cache
        def dfs(node):
            nonlocal res
            if not node:
                return
            
            if not node.left and not node.right:
                res.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root1)
        res1 = res
        res = []
        dfs(root2)

        return res == res1