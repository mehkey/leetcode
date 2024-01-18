class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M = len(grid)
        N = len(grid[0])
        for _ in range(k):
            
            prev = grid[M-1][N-1]
            
            for i in range(M):
                for j in range(N):
                    
                    temp = grid[i][j]
                    grid[i][j] = prev

                    prev = temp
        
        return grid