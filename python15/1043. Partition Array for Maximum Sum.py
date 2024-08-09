class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        nums = []
        N = len(arr)
        res = [0]*N

        @cache
        def dp(i):

            if i == N:
                return 0

            #count = 1

            curMax = curSum = 0

            for j in range(i,min(N,i+k)):
                
                curMax = max(curMax, arr[j])
                cur = curMax * (j - i + 1) + dp(j + 1)
                curSum = max(curSum, cur)

            return curSum

        return dp(0)
