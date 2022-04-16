class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #print(nums[1:])
        #print(nums[:-1])
        
        def rob( nums: List[int]) -> int:
        
            # the 2 previous
            rob1, rob2 = 0,0

            for i in range(len(nums)):
                tmp = max(rob1 +nums[i], rob2)
                rob1 = rob2
                rob2 = tmp

            return rob2
        
        #print(rob(nums[1:]))

        return max(nums[0], rob(nums[1:]), rob(nums[:-1]))
        