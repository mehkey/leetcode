# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(node:TreeNode,min_node_value:int, max_node_value:int) -> int:

            if not node:
                return abs(min_node_value-max_node_value)
            
            min_node_value = min(min_node_value, node.val)
            max_node_value = max(max_node_value, node.val)

            return max(dfs(node.left,min_node_value,max_node_value),
            dfs(node.right,min_node_value,max_node_value))

        return dfs(root,root.val,root.val)
