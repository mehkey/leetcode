class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        nums = []
        N = len(arr)
        res = [0]*N

        @cache
        def dp(i):

            if i == N:
                return 0


            curMax = curSum = 0

            for j in range(i,min(N,i+k)):
                
                curMax = max(curMax, arr[j])
                cur = curMax * (j - i + 1) + dp(j + 1)
                curSum = max(curSum, cur)

            return curSum

        return dp(0)


        N = len(arr)
        K = k + 1

        dp = [0] * K

        for start in range(N - 1, -1, -1):
            curr_max = 0
            end = min(N, start + k)

            for i in range(start, end):
                curr_max = max(curr_max, arr[i])
                dp[start % K] = max(dp[start % K], dp[(i + 1) % K] + curr_max * (i - start + 1))

        return dp[0]