


class Solution:
    def numSquares(self, n: int) -> int:

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            min_val = float('inf')
            j = 1
            while j * j <= i:
                min_val = min(min_val, dp[i - j * j] + 1)
                j += 1
            dp[i] = min_val
        return dp[n]


        root = []

        for i in range(1, ceil(sqrt(n ) + 1)):
            root.append(i*i)

        root = list(reversed(root))

        #print(root)
        count = 0
        res = 0
        for i in range(len(root)):
            while count + root[i] <= n:
                count += root[i]
                res += 1
                if count == n:
                    return res 
            
        return 0
        '''
        #@cache
        def dp(i,cur):
            if cur == n:
                return 0

            if i == len(root):
                return inf

            if cur > n:
                return inf

            return min(dp(i,cur+root[i])+1, dp(i+1,cur))
        '''
        return dp(0,0)
