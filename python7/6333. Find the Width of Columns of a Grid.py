
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        M = len(grid)
        N = len(grid[0])
        
        res = []
        for i in range(N):
            m = 0
            for j in range(M):
                n = grid[j][i]
                if n >= 0:
                    m = max(m,len(str(n)))
                else:
                    m = max(m,len(str(n)))
            res.append(m)
        
        return res
return [max(len(str(a)) for a in r) for r in zip(*A)]