class Solution:
    def minimumMoves(self, gggg: List[List[int]]) -> int:
        
        @cache
        def dp(grid):
            
            if all([grid[x][y] == 1 for x in range(3) for y in range(3) ]):
                return 0
            
            z= set()
            g=set()
            for x in range(3):
                for y in range(3):
                    if grid[x][y] == 0:
                        z.add((x,y))
                    if grid[x][y] >1 :
                        g.add((x,y))
            
            res = float('inf')
            for x0,y0 in z:
                for xg,yg in g:
                    gg = list(list(i) for i in grid)
                    
                    gg[x0][y0] = 1
                    gg[xg][yg] -= 1
                    
                    ggt = tuple(tuple(i) for i in gg)
                    
                    res = min(res, dp(ggt) + abs(x0-xg) + abs(y0-yg))
            
            return res
                    
        ggggt = tuple(tuple(i) for i in gggg)
        
        return dp(ggggt)