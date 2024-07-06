class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        
        m = inf
        
        for j,pp in enumerate(position):
            
            t = 0
            
            for i,p in enumerate(position):
                if abs(pp-p) % 2 == 1:
                    t += 1 
            
            #print(t)
            m = min(m,t)
        
        
        
        return m