class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        M = len(grid)
        N = len(grid[0])
        
        dirs = [[-1,1],[0,1],[1,1]]
        
        @cache
        def dfs(i,j):

            ma = 0
            for d in dirs:
                ni = i + d[0]
                nj = j + d[1]
                
                if 0 <= ni < M and 0 <= nj < N and grid[i][j] <grid[ni][nj]:
                    ma = max( dfs(ni,nj) + 1 , ma)
                
            return ma
            
        
        res = 0
        
        for i in range(M):
            
            res = max( dfs(i,0), res )
            
        return res