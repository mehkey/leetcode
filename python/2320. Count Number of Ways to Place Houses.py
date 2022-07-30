class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 10**9 + 7
        """
        dp = [0] * (n+1)
        dp[0] =1
        dp[1] =9
        dp[2] =25
        
        for i in range(1,n+1):

            dp[i] = (dp[i-1] + dp[i-1]**2%mod ) % mod

        return dp[n]% mod
        """
        #if n ==1:
        #    return 4
        #return (n*2 -1) ** 2 %mod
        @cache
        def fib(n):
            if n == 1:
                return 2
            if n == 0:
                return 1
            return fib(n-1) + fib(n-2) %mod
        
        return fib(n)**2 %mod

#1 22 4
#2 33 9
#3 55 25
#4 77 49
#5 13 169
