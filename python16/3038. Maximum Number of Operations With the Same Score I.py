class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        

        add = 1
        sc = nums[0] + nums[1]
        
        nums = deque(nums)
        nums.popleft()
        nums.popleft()
        
        while len(nums) >= 2:
            
            first = nums.popleft()
            sec = nums.popleft()
            if sc != first + sec:
                return add
            
            add += 1
        
        return add