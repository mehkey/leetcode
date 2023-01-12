class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        nums =[-i for i in nums]
        heapify(nums)
        
        t = 0
        while k:
            #print(nums)
            v = - heappop(nums)
            t+=v
            k-=1
            heappush(nums,- ceil(v / 3) )
        
        return t
        
        