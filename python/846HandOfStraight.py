class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        hm = {}
        
        for c in hand:
            hm[c] = hm.get(c,0) + 1
        
        q = []
        q = list(hm.keys()).copy()
        
        heapq.heapify(q)
        
        #print(q)
        #print(heapq.heappop(q))
        
        while q :
            top = q[0]
            hm[top] -= 1
            
            #print(top)
            
            if hm[top] < 0:
                return False

            if hm[top] == 0:
                heapq.heappop(q)
            
            for i in range(1, groupSize):
                
                if  hm.get(top+i,-1) <= 0:
                    return False

                hm[top+i] -= 1

                if hm[top+i] == 0:
                    heapq.heappop(q)
            
        
        return True
            
            