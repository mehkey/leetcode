class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        c = 0
        while not all([nums[i] < nums[i+1] for i in range(0,len(nums)-1)]):
            #nums.append(nums[0])
            nums = [nums[-1]] + nums[:-1]
            c+=1
            if c == len(nums):
                return -1
        
        return c