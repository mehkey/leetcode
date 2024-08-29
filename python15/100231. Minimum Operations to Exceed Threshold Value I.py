class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(n < k for n in nums)

        nums.sort()
        
        nums = deque(nums)
        m = min(nums)
        
        o = 0
        
        while m < k:
            
            o += 1
            
            nums.popleft()
            
            m = nums[0]
            
            
            
        return o