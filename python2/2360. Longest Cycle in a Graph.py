class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        v = set()
        
        res = -1
        
        for n in range(len(edges)):

            j = 0
            
            prev = {}
            
            while n != -1 and n not in v:
                prev[n] = j
                j+=1
                v.add(n)
                n = edges[n]
            
            if n != -1 and n in prev:
                res = max(res, j - prev[n])
        
        return res
