class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        
        nums.sort()
        
        diff = float('inf')
        
        for i in range(0,len(nums)-1):
            
            diff = min(diff, nums[i+1]-nums[i])
        
        return diff