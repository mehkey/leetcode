class Solution:
    def maximumBags(self, c: List[int], r: List[int], a: int) -> int:
        
        t = 0
        
        d=[]

        for i in range(len(c)):
            dd = c[i] - r[i]
            if dd == 0:
                t += 1
            else:
                d.append(dd)
        
        heapify(d)
        
        while d:
            
            dd = heapq.heappop(d)
            
            a -= dd
            if a < 0:
                break
            
            t+= 1
        
        return t
                
        
        return t
        