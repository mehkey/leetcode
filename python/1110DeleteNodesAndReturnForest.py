# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        
        forest = []
        
        to_del = set(to_delete)
        
        def dfs(root,inForest):
            if not root:
                return None

            if root.val in to_del:
                
                root.left = dfs(root.left,False)
                root.right = dfs(root.right,False)
                return None
            else:

                if not inForest:
                    forest.append(root)

                root.left = dfs(root.left,True)
                root.right = dfs(root.right,True)
                return root

        dfs(root, False)
        
        return forest