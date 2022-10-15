class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        ma = 0
        
        def total(i,j):
            dirs = [[0,0],[1,0],[-1,0],[-1,-1],[1,1],[-1,1],[1,-1]]
            t = 0
            for d in dirs:
                t += grid[i+d[0]][j+d[1]]
            
            return t
        
        for i in range(1,m-1):
            for j in range(1,n-1):
                ma = max(ma, total(i,j))
                
                

        return ma