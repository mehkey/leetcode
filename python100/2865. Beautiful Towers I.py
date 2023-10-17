class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        
        l = 0
        mm = len(maxHeights)
        
        mmm = 0
        
        for start in range( mm ):

            l = start -1
            r = start +1
            
            tot = maxHeights[start]
            cur = tot
            while l >= 0 :
                
                cur = min(cur,maxHeights[l])
                tot += cur
                l-= 1
            cur = tot
            while r <= len(maxHeights) -1:
                cur = min(cur,maxHeights[r])
                tot += cur
                r+= 1
            
            mmm = max(mmm, tot)
        return mmm
