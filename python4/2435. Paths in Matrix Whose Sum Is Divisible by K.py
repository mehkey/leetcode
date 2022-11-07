class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:

        m = len(grid)
        n = len(grid[0])
        
        mod = 10**9 + 7
        
        k = k

        tmp = [[defaultdict(int) for i in range(len(grid[0]))] for j in range(len(grid))]

        tmp[0][0][grid[0][0] %k] = 1
        

        for i in range(1,len(grid)):
            
            s = tmp[i-1][0].keys() 
            tmp[i][0][(list(s)[0] +grid[i][0]) %k] =1
            
            

        for j in range(1,len(grid[0])):
            
                
            s = tmp[0][j-1].keys() 
            tmp[0][j][(list(s)[0] + grid[0][j])%k] = 1

        for i in range(1,len(grid)):
            
            for j in range(1,len(grid[0])):
                for l in tmp[i-1][j].keys():
                    s1 = tmp[i-1][j][l] #+ grid[i][j]
                    tmp[i][j][(l+grid[i][j])%k] += s1 % mod

                for l in tmp[i][j-1].keys():
                    s1 = tmp[i][j-1][l] #+ grid[i][j]
                    tmp[i][j][(l+grid[i][j])%k] += s1 % mod

        return tmp[m-1][n-1][0] % mod