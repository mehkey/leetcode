class Solution:
    def minimumTime(self, s: str) -> int:
        
        min_cost = 0
        cost = 0
        for c in s:
            
            if c == '1':
                cost = min(1,cost+1)
            else:
                cost = min(-1,cost-1)
            
            min_cost = min(min_cost,  cost)
        
        return len(s) + min_cost
    
    
        def minSum(nums):
            dp, dp_min = nums[0], nums[0]
            for i in range(1, len(nums)):
                dp = min(nums[i], nums[i] + dp)
                dp_min = min(dp, dp_min)
            return min(0, dp_min)
        return len(s) + minSum([1 if i == "1" else -1 for i in s])

    

    def minimumTime(self, s):
        left, res, n = 0, len(s), len(s)
        for i,c in enumerate(s):
            left = min(left + (c == '1') * 2, i + 1)
            res = min(res, left + n - 1 - i)
        return res