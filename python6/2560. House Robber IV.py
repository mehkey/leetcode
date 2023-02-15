class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:


        def target(t):
            i ,count= 0,0
            while i < len(nums):
                if nums[i] <= t:
                    count += 1
                    i+=1
                i+=1

            return count >= k
            
        l = 0
        r = max(nums)
        
        m = float("inf")
        
        while l <= r:
            
            mid = (l+r)//2
            
            if target(mid):
                m = min(m,mid)
                r = mid -1
            else:
                l = mid +1
        
        return m if m != float("inf") else -1