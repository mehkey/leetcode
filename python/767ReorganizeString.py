class Solution:
    def reorganizeString(self, s: str) -> str:
        
        hm = {}
        
        for c in s:
            hm[c] = hm.get(c,0) - 1

        heap = []
        for c in hm:
            heap.append([hm[c],c])

        heapq.heapify(heap)
        
        previous = None
        
        res = ""
        
        while previous or heap:
            
            if previous and not heap:
                return ""
            
            val = heapq.heappop(heap)
            
            res += val[1]
            val[0] += 1
            
            if previous :
                heapq.heappush(heap, previous)
                previous = None
            
            if val[0] != 0 :
                previous = val
        
        return res
