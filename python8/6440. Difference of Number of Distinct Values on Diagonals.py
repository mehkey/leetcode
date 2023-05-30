class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        M = len(grid)
        N = len(grid[0])

        res = [[0 for i in range(N)] for j in range(M)]

        for i in range(M):
            for j in range(N):
                
                top = set()
                
                k = 1
                
                while i -k >=0 and j -k >=0:
                    top.add(grid[i-k][j-k])
                    k+=1
                
                bot = set()
                
                k =1
                
                while i +k < M and j +k < N:
                    bot.add(grid[i+k][j+k])
                    k+=1
                
                res[i][j] = abs(len(top)-len(bot))
        
        return res
                