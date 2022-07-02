class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        
        
        """
        
        1 3 2 5 4
        
        1 3 2
        
        
        1 2  6 7 8
        
        1 7 --- 4 5 3 2 2
        
        1 7 --- 2 3 45
        
        O(n!)
        
        dp[(1,3,2)] = [max, number]
        
        
        dp(1) = [1,1]
        dp(2) = [2,1]
        dp(3) = [3,1]

        dp(whatever) = [ max(numbers) , dp(whatever - last) + 1 if increasing ]

        dp[1][1] = 1
        
        dp[n][k] = dp[n-1][k-1] +  (n-1)* dp[n-1][k]
        
        
        
        dp = {[[0 for i in range(k+1)] for j in range(n+1)]}
        dp[0][0] = 0
        dp[0][1] = 0
        dp[1][1] = 1
        
        def dfs(n,k):
            
            if n == 0 or k == 0:
                return 0
            
            if dp[n][k] != 0:
                return dp[n][k]
            
            p1 = dfs(n-1,k-1)
            p2 = (n-1) * dfs(n-1,k)
            val = p1 + p2
            dp[n][k] = val
            return val
        
        return dfs(n,k) % (10**9+7)
        
        
        dp = {}
        dp[(0,0)] = 0
        dp[(0,0)] = 0
        dp[(1,1)] = 1
        
        def dfs(n,k):
            
            if n == 0 or k == 0:
                
                return 0
            
            if (n,k) in dp:
                return dp[(n,k)]
            
            p1 = dfs(n-1,k-1)
            p2 = (n-1) * dfs(n-1,k)

            val = p1 + p2
            dp[(n,k)] = val
            return val
        
        return dfs(n,k) % (10**9+7)
        
        """
        
        
        dp = {}
        dp[(0,0)] = 0
        dp[(0,0)] = 0
        dp[(1,1)] = 1
        
        for N in range(2,n+1):
            for K in range(1,k+1):

                p1 = dp.get((N-1,K-1),0)
                p2 = (N-1) * dp.get((N-1,K),0)

                val = p1 + p2
                dp[(N,K)] = val

        return dp[(n,k)] % (10**9+7)
        
        