class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        if a > b:
            a,b = b,a
        
        res = 0
        for i in range(1,a+1):
            #print(b/i)
            if ( b / i ) % 1 == 0 and (a/i) % 1 == 0:
                res +=1
        
        return res