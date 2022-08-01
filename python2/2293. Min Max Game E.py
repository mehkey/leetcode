class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        while len(nums) > 1:
            tmp = []
            m = True
            for i in range(0,len(nums),2):
                if m:
                    tmp.append(min(nums[i],nums[i+1]))
                else:
                    tmp.append(max(nums[i],nums[i+1]))
                m = not m

            nums = tmp
        
        return nums[0]