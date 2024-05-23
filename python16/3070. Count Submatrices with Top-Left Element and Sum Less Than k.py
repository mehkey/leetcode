class Solution:



    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
        self.m = grid

        M = len(grid)
        N = len(grid[0])
        
        s = 0
        
        res = 0
        for i in range(0, M):
            for j in range(0 , N):

                
                if i > 0 and j > 0:
                    self.m[i][j] +=  self.m[i-1][j] + self.m[i][j-1] - self.m[i-1][j-1]
                elif i> 0:
                    self.m[i][j] +=  self.m[i-1][j] 
                elif j>0:
                    self.m[i][j] +=  self.m[i][j-1] 
                
                if self.m[i][j] <= k:
                    res += 1
        
        return res
