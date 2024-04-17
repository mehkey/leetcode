class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        g = [[0]*n for _ in range(m)]
        
        for r,c in indices:
            
            for j in range(n):
                g[r][j] += 1 
                g[r][j] %= 2
            for i in range(m):
                g[i][c] += 1
                g[i][c] %= 2
            
        return sum(sum(g,[]))