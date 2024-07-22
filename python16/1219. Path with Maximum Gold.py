class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        M = len(grid)
        N = len(grid[0])
        def dfs(i,j, path):
            
            #if (i,j) in path:
            #    return 0
            
            dirs = (-1,0,1,0,-1)
            #mv = grid[i][j]
            mv = 0
            for l in range(4):
                ni = i + dirs[l]
                nj = j + dirs[l+1]
                
                if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] > 0 and (ni,nj) not in path:
                    path.add((i,j))
                    mv = max(dfs(ni,nj,path),mv)
                    path.remove((i,j))
            
            return grid[i][j] + mv

        mv = 0
        
        for i in range(M):
            for j in range(N):
                
                mv = max(mv, dfs(i,j,set()))
                
        return mv
        
        
        