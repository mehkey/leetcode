class Solution:
    def maxStrength(self, nums: List[int]) -> int:

        def dp(cur,i):
            if i == len(nums):
                return cur

            return max(dp(cur,i+1), dp(cur*nums[i], i+1))

        m = float('-inf')
        for i,n in enumerate(nums):
            m = max(dp(n,i+1),m)

        return m
