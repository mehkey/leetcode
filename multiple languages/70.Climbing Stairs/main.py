class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        prev_prev = 1
        prev = 2
        for i in range(n-2):
            result = prev_prev + prev
            prev_prev = prev
            prev = result
        return result



        '''
        top = 1
        last = 2
        previous_last = 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        for i in range(n-1):
            previous_last, last,top = last+top, previous_last, last

        return previous_last

        

        dp = {}
        dp[n-1] = 1
        dp[n-2] = 2

        def dfs(i):

            if i in dp:
                return dp[i]
            
            if i > n:
                return 0

            dp[i] = dfs(i+1) + dfs(i+2)

            return dp[i]

        dfs(0)

        #print(dp)

        return dp[0]

        

        return int(round(1/5**0.5 * (((1+5**0.5)/2.0)**(n+1) - ((1-5**0.5)/2.0)**(n+1))))
        '''



        