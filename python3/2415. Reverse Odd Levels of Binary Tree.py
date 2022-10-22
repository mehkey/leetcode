# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        q = Deque()
        q.append(root)
        level = 1
        
        while q:
               
            lev = []

            for _ in range(len(q)):

                n = q.popleft()

                if n.left is not None:
                    q.append(n.left)
                    lev.append(n.left)
                if n.right is not None:
                    q.append(n.right)
                    lev.append(n.right)

            if level %2 == 1:
                tot = len(lev)
                for i,l in enumerate(lev):
                    if i >= tot //2:
                        break
                    lev[i].val, lev[tot-1-i].val = lev[tot-1-i].val, lev[i].val

            level += 1
        
        return root
                
                
        '''
        def dfs(node, level):
            
            if not node:
                return 
            
            if level %2 == 1:
                
                if not node.left or not node.right:
                    return 

                l = node.left.val
                r = node.right.val
                
                node.left.val = r
                node.right.val = l
                
                dfs(node.left, level+1)
                dfs(node.right, level+1)
            
            else:
                
                dfs(node.left, level+1)
                dfs(node.right, level+1)

        dfs(root,1)
        '''
        #return root