class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(mid):
            bucket = 0
            totalBuckets = 1
            
            for w in weights:
                if bucket + w > mid:
                    bucket = w
                    totalBuckets += 1
                else:
                    bucket += w

            return totalBuckets  
        
        #binary search
        
        l = max(weights)
        
        r = sum(weights)
        
        res = r
        
        while l <= r :
            mid = (r+l) // 2
            
            if check(mid) <= days  :
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res