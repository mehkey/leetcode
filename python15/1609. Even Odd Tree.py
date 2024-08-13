# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        
        
        q = deque()
        
        q.append(root)
        
        l = 0
        
        
        while q:
            
            l+=1
            ql = len(q)
            po = 0
            pe = inf
            for _ in range(ql):
                
                cur = q.popleft()
                
                if cur.val % 2 == 0 and l % 2 == 1:
                    return False
                
                if cur.val % 2 == 1 and l % 2 == 0:
                    return False
                
                if l % 2 == 1:
                    if cur.val <= po:
                        return False
                    po = cur.val
                else:
                    if cur.val >= pe:
                        return False
                    pe = cur.val
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return True
