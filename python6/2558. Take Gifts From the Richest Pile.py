class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        
        gifts = [-g for g in gifts]
        heapify(gifts)
        
        for i in range(k):
            
            if not gifts:
                return 0
            
            left = -heappop(gifts)

            heappush(gifts,-floor(sqrt(left)))
            
        
        return -sum(gifts)