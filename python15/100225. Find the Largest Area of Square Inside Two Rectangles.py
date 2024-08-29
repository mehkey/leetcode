class Solution:
    def largestSquareArea(self, bl: List[List[int]], tr: List[List[int]]) -> int:
        
        N = len(bl)
        ma = 0
        
        for i in range(N):
            for j in range(i+1,N):
                
                lx = max(bl[i][0], bl[j][0]) #tr[i][0])
                ly = max(bl[i][1], bl[j][1]) #tr[i][1])
                
                rx = min(tr[i][0], tr[j][0])
                ry = min(tr[i][1], tr[j][1])
                
                if lx < rx and ly < ry:
                    ma = max(ma, min(rx-lx, ry-ly)**2)
        
        return ma