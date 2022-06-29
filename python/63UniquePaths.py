class Solution:
    def uniquePathsWithObstacles(self, og: List[List[int]]) -> int:
        
        """
        
        DFS
        
        Dynamic programming
        
        
        """
        if og[0][0] == 1:
            return 0
        
        m = len(og)
        n = len(og[0])
        
        dp = [[0 for i in range(n)]for j in range(m)]
        dp[0][0] = 1
        
        #print(dp)
        
        for i in range(m):
            if og[i][0] == 1:
                break
            dp[i][0] = 1
        
        for j in range(n):
            if og[0][j] == 1:
                break
            dp[0][j] = 1
            
        for i in range(1,m):
            for j in range(1,n):
                if og[i][j] != 1:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        #print(dp)
        
        return dp[m-1][n-1]