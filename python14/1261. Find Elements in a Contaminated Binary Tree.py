# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.s = set()
        def cur(node,val):
            if not node:
                return
            
            node.val = val
            self.s.add(val)
            
            if node.left:
                cur(node.left, val*2 + 1)
            
            if node.right:
                cur(node.right, val*2 + 2)
        
        cur(root,0)

    def find(self, target: int) -> bool:
        
        return target in self.s

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)