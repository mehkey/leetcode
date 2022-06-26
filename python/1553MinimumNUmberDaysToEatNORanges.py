class Solution:
    def minDays(self, n: int) -> int:
        
        
        
        
        """
        
        n = 10
        
        O O O O O O O O O O
        
        day 1 O O O O O
        
        day 2 O O O O
        
        day 3 0 0
        
        day 4 0
        
        day 5 0
        
        
        
        0 0 0 0 0 0 0 0 0 0 0
        
        - path1
        - path2
        - path3
        
        0 0 0 0 0 0 0 0 
        
        - path1
        - path2
        - path3
        
        

        
                   |
            |      |.     |
           | | |  | |.  | |. |
           ...    ...    ...
           
           
        BFS 
        
        O ( 3 ^ n)
        
        
        
        9 oranges
        6 oranges
        
        3 oragnes
        
        dp[1] = 1
        dp[0] = 0
        
        dp[nOranges] = min(dp[nOranges/3] + nOranges%3,  dp[nOranges/2]+ nOranges%2)
        

        def dp(nOranges):
            if nOranges == 0:
                return 0
            
            if nOranges == 1:
                return 1
            
            return min(dp(nOranges//3) + nOranges%3 + 1,  dp(nOranges//2)+ nOranges%2 + 1)
        
        return dp(n)
        
        
        
        
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2,n+1):
            
            dp[i] = min(dp[i//3] + i%3 + 1,  dp[i//2]+ i%2 + 1)
        
        return dp[n]"""
        
        dp = {}
        dp[1] = 1
        dp[0] = 0
        
        def dfs(nOranges):
            if nOranges in dp:
                return dp[nOranges]
            
            dp[nOranges] =  min(dfs(nOranges//3) + nOranges%3 + 1,  dfs(nOranges//2)+ nOranges%2 + 1)
            return dp[nOranges]
        
        dfs(n)
        
        return dp[n]