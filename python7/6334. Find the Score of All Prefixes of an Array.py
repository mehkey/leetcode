class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:

        ans = [0] * len(nums)
        
        if len(nums) == 0:
            return []

        m = 0
        for i,v in enumerate(nums):
            m = max(m,v)
            ans[i] = v + m + ans[i-1]
        
        return ans
        
        