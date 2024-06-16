class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        N = len(nums)

        @cache
        def dp(s,e, sc):
            if s >= e or e < 0 or s < 0 or e >= N or s >= N:
                return 0
            
            res = 0
            
            
            if nums[s] + nums[e] == sc:
                res = max(res, dp(s+1,e-1,sc) + 1)
            
            if s + 1 < N and nums[s] + nums[s+1] == sc:
                res = max(res, dp(s+2,e,sc) + 1)
            
            if e-1 >= 0 and nums[e] + nums[e-1] == sc:
                res = max(res, dp(s,e-2,sc) + 1)
            
            return res

        return max(  dp(0,len(nums)-1, nums[0] + nums[N-1] ),  dp(0,len(nums)-1, nums[0] + nums[1] ),  dp(0,len(nums)-1, nums[N -2] + nums[N-1] ) )