class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #piles = [3,6,7,11]
        #h = 8

        #k = [i for i in range(1,max(piles))]

        #k = [1,2,3,4,5,6,7,8,9,10,11]
        
        if len(piles) == 1 and h > piles[0]:
            return 1
        
        l = 0
        r = max(piles) 
        
        res = r
        
        while(l <= r):
            
            #print(l , " ",r)
            mid = (l+r) // 2
            
            total = 0
            for bananas in piles:
                total = total+ math.ceil(bananas/(mid if mid > 0 else 1))
            
            if total <= h:
                res = min(res, mid)
                r = mid -1
            else :
                l = mid + 1
        
        return res