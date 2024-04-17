class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        N= len(grid)
        M = len(grid[0])
        for r in range(1,N):

            for c in range(0,M):
                mid = grid[r-1][c]
                left = grid[r-1][c-1] if c > 0 else inf
                right = grid[r-1][c+1] if c < M -1 else inf
                grid[r][c] += min(mid,left,right)
        return min(grid[-1])
