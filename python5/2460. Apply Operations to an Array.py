class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        

        for i,n in enumerate(nums):
            
            if i < len(nums)-1:
                
                if nums[i] == nums[i+1]:
                    nums[i] *= 2
                    nums[i+1] = 0

        return list(filter(lambda x: x > 0, nums)) + [0] * nums.count(0) 
        