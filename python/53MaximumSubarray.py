class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        """
        l = 0
        
        r = 0
        
        m = float("-inf")
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                m = max(m,sum(nums[i:j+1]))
        
        return m
        
        """
        m = nums[0]
        currentsum = 0
        
        for i in range(len(nums)):
            if currentsum < 0:
                currentsum = 0

            currentsum += nums[i]
            m = max(m,currentsum)

        return m