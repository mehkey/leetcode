class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        h = defaultdict(int)
        l = 0
        s = -1
        e = -1
        for r in range(len(nums)):
            h[nums[r]]+=1
            kv = -1
            if h[nums[r]] > k:
                kv = nums[r]
            
            #print(h)
            while l < len(nums) and h[kv] > k: #not all(i <= k for i in h.values()):
                
                #if s == -1 or r-l > e-s:
                #    s= l
                #    e= r
                
                h[nums[l]]-=1
                l+=1
            
            if s == -1 or r-l > e-s:
                s= l
                e= r
        
        return e - s + 1