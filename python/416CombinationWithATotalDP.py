class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        
        """
        [1,5,1,20]
        
        
        [1] [5,1,20]
        [1,5] [1,20]
        
        
        
        
        
        for i in range(0, len(nums)):
            
            left = nums[0:i]
            right = nums[i+1:]
            
            if (sum(left) == sum(right)):
                return True
            
        return False
        
        """
        t = sum(nums)
        if t %2 != 0:
            return False
        
        
        dp = set()
        target = t //2
        dp.add(0)
        for i in range(0, len(nums)):
            newdp = set()
            for val in dp:
                newdp.add(val+nums[i])
                newdp.add(val)
            
            dp = newdp

        
        return True if target in dp else False
            
        
            