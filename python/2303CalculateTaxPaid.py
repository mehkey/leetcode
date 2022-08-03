class Solution:
    def calculateTax(self, b: List[List[int]], i: int) -> float:
        
        t = 0.0
        c = 0
        for u,p in b:
            #m = i - u
            #if  <0:
            #print(u,p)
            if i > u:
                
                t += (u -c) * p / 100
                #i = i - u
                c = u
            else:
                t += (i - c) * p / 100
                break
            
            #print(t)
            
        return t