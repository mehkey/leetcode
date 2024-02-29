class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        
        res = 0
        md = 0
        
        sol = []
        for l,r in dimensions:
            
            d = sqrt(l*l + r*r)
            sol.append((d,l*r))

        sol.sort()
        return sol[-1][1]