class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        '''
        nums.sort()
        
        return nums[0] + nums[1] + nums[2]
        '''
        
        i = 0
        j = 1
        k = 2
        
        res = inf
        N = len(nums)
        @cache
        def dp(j,k):
            if  j ==k or k == N:
                return inf
            val = nums[0] + nums[j] + nums[k]
            return min(val,  dp(j+1,k),dp(j,k+1))
        
        return dp(1,2)