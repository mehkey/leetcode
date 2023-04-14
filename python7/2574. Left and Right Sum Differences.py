class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums)
        
        count = 0
        for i in  range(1,len(nums)):
            count += nums[i-1]
            res[i] += count
 
        count = 0
        for i in  range(len(nums)-2,-1,-1):
            count += nums[i+1]
            res[i] = abs( count - res[i])
        #for i,n in enumerate(reversed(nums)):
        #    res[len(nums)-i-1] -= nums[i-1]
            
        return res
            