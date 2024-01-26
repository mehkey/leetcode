class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        
        MOD = 10**9+7

        @cache
        def dp(i, highInd, highVal):
            
            if i == n:
                return highInd == k

            if highInd > k:
                return 0
            
            if k == highInd:
                res = (highVal ) * dp(i+1,highInd,highVal) 

                return res % MOD
            
            res = 0
            for j in range(1,m+1):
                
                if j > highVal:
                    
                    res += dp(i+1, highInd+1, j )
                
                else:
                    res += dp(i+1, highInd, highVal)
            
            return res % MOD
        
        return dp(0,0,-1)
