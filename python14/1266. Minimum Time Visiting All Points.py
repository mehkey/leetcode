class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        res = 0
        px,py = points[0][0], points[0][1]
        for x,y in points:
            
            res += max( abs(px-x), abs(py-y))
            #print(res)
            
            px,py = x,y
            
            
        
        return res