class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        n = len(nums);ans = 0
        dp = defaultdict(Counter)
        for i in range(1,n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] += dp[j][d] + 1
            ans += sum(dp[i].values()) - i
        return ans

        nums.sort()

        N = len(nums)

        s = set(nums)

        @cache
        def dp(i):

            res = 0

            for j in range(i+1,N):
                
                diff = nums[j] - nums[i]

                if diff + nums[j] in s:
                    res += 1
            return res

        res = 0
        
        return dp(0)