class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        

        nums.sort()
        
        o = 0
        
        if nums[0] >= k:
            return 0
        
        while True: #m < k:
            
            o += 1
            
            l1 = heappop(nums)
            l2 = heappop(nums)
            
            heappush(nums, min(l1,l2)*2 + max(l1,l2))
            
            m = nums[0]
            
            #print(nums)
            if m >= k:
                break
            
        return o