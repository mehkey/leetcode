# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> Optional[TreeNode]:
        if not pre or not post: return None
        root = TreeNode(pre[0])
        if len(post) == 1: return root
        idx = pre.index(post[-2])
        print(idx)
        root.left = self.constructFromPrePost(pre[1: idx], post[:(idx - 1)])
        root.right = self.constructFromPrePost(pre[idx: ], post[(idx - 1):-1])
        return root