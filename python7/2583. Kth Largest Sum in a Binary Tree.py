# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        
        q = deque()
        
        
        q.append(root)
        
        l = 0
        
        h = []
        
        while q:

            s = len(q)
            summ = 0
            
            for _ in range(s):
                
                cur = q.popleft()
                
                summ += cur.val
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            heappush(h,-summ)
        
        for i in range(k-1):
            heappop(h)
            if not h:
                return -1
        
        return -h[0]
                