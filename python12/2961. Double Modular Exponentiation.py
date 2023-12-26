class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        
        r = []
        
        for i,(a,b,c,m) in enumerate(variables):
            
            res = pow( pow(a,b,10) , c , m)  
            if res == target:
                r.append(i)
        
        return r