# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        l = 0
        r = n-1
        
        u = 0
        d = m -1
        
        res = [[-1 for i in range(n)] for j in range(m)]
        
        #print(res)
        
        def dfs(l,r,u,d,head):
            
            if l > r and u > d:
                return
            
            for j in range(l,r):
                res[u][j] = head.val
                head = head.next
                if not head:
                    return
            
            for i in range(u,d):
                res[i][r] = head.val
                head = head.next
                if not head:
                    return
            
            for j in range(r,l-1,-1):
                res[d][j] = head.val
                head = head.next
                if not head:
                    return

            for i in range(d-1,u,-1):

                res[i][l] = head.val
                head = head.next
                if not head:
                    return
            
            dfs(l+1,r-1,u+1,d-1,head)

        dfs(l,r,u,d,head)
        
        return res


def spiralMatrix(self, m, n, head):
    matrix = [[-1 for _ in range(n)] for _ in range(m)]
    
    x, y = 0, 0
    dx, dy = 0, 1
    
    cur = head
    
    while cur:
        matrix[x][y] = cur.val
        
        if (x + dx < 0) or (x + dx >= m) or (y + dy < 0) or (y + dy >= n) or (matrix[x + dx][y + dy] != -1):
            dx, dy = dy, -dx
            
        x += dx
        y += dy
        
        cur = cur.next
        
    return matrix