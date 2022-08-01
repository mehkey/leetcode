class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)

        prev = nums[0]
        
        ans = 1
        
        for i in range(1,len(nums)):
            diff = abs(nums[i]- prev)
            
            if diff > k:
                ans +=1
                prev = nums[i]
        
        return ans