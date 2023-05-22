class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        
        nums.sort()
        #print(nums)
        
        if len(nums) <= 3:
            return 0
        #print(nums[-3])
        if abs(nums[0] - nums[-3]) <= abs(nums[1]-nums[-2]) and abs(nums[0] - nums[-3]) <= abs(nums[2] - nums[-1]) :

            return abs(nums[0] - nums[-3]) 
        
        if abs(nums[1]-nums[-2])  <= abs(nums[0] - nums[-3])  and abs(nums[1]-nums[-2])  <= abs(nums[2] - nums[-1]):
            return abs(nums[1]-nums[-2])
        
        
        if abs(nums[2] - nums[-1])  <= abs(nums[0] - nums[-3])  and abs(nums[2] - nums[-1])  <= abs(nums[1]-nums[-2]):
            return abs(nums[2] - nums[-1]) 

        
        '''
        
        if abs(nums[0] - nums[-2]) > abs(nums[-1]-nums[1]):
            nums.pop(0)
        else:
            nums.pop()

        print(nums)
        return abs(nums[-1]-nums[0]) 
        '''

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[-2] - nums[1],
                   nums[-1] - nums[2],
                   nums[-3] - nums[0])