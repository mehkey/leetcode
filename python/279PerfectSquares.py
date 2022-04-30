class Solution:
    def numSquares(self, n: int) -> int:

        dp = [n] * (n+1)
        dp[0]=0

        for target in range(1, n+1):
            for j in range(1, target):

                square = j * j

                if target - square < 0 :
                    break

                dp[target] = min(dp[target], 1 + dp[target - square])

        return dp[n]