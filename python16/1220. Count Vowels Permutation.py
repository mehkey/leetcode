class Solution:
    def countVowelPermutation(self, n: int) -> int:
        M = 10**9 + 7
        @cache
        def dp(i,cur):
            if i == n:
                return 1
            
            if cur == 'a':
                return dp(i+1,'e') % M
            if cur == 'e':
                return (dp(i+1,'a') + dp(i+1,'i')) % M
            if cur == 'i':
                return (dp(i+1,'a') +  dp(i+1,'e') +dp(i+1,'o') +dp(i+1,'u') )% M
            
            if cur == 'o':
                return (dp(i+1,'i') +  dp(i+1,'u') ) % M
            
            if cur == 'u':
                return (dp(i+1,'a')) % M
                
        mv = 0
        
        for c in 'aeiou':
            mv +=  (dp(1,c) % M )
        
        return mv% M 

        MOD = 10 ** 9 + 7
        dp = [[0] * 5 for _ in range(n)]
        for i in range(5):
            dp[0][i] = 1
        for i in range(1, n):
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]) % MOD
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD
            dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % MOD
            dp[i][3] = dp[i - 1][2]
            dp[i][4] = (dp[i - 1][2] + dp[i - 1][3]) % MOD
        return sum(dp[-1]) % MOD