class Solution:
    def minimumCoins(self, p: List[int]) -> int:
        n = len(p)

        @cache
        def dp(i):

            if i >= n:
                return 0
            
            m = inf
            for j in range(i+1, min( (i+1) + (i+1) + 1  ,n+1)):
                #print(i, j)
                m = min(m,  dp(j) + p[i] )
                #return min(p[i] + dp(i+2), p[i] + dp(i+1))
            
            #print("m", i,m)
            return m 

        return dp(0)
        