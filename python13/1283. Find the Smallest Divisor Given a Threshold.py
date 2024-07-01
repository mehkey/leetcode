class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        N = len(nums)
        l = 1
        r = max(nums)
        
        t = inf
        while l <= r:
            mid = (l+r)//2
            
            res = sum([ ceil( n / mid ) for n in nums])
            
            if res <= threshold:
                r = mid - 1
                t = min(t, mid)
            else:

                l = mid + 1
        
        return t
    

