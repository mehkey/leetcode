class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        M = len(grid)
        N = len(grid[0])

        dirs = ((1,0),(0,1),(-1,0),(0,-1))
        m = 0
        
        for i in range(M):
            for j in range(N):
                
                v = set()
                
                def dfs(i,j):
                    if grid[i][j] == 0:
                        return 0

                    t = grid[i][j]
                    
                    for d in dirs:
                        ni = i + d[0]
                        nj = j + d[1]
                        
                        if 0 <= ni < M and 0 <= nj < N and (ni,nj) not in v and grid[ni][nj] > 0:
                            v.add((ni,nj))
                            t += dfs(ni,nj)
                    
                    return t
                
                v.add((i,j))
                
                m = max(m,dfs(i,j))

        
        return m